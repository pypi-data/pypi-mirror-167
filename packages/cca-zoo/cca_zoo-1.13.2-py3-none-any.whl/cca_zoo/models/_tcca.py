from typing import Iterable, Union

import numpy as np
import tensorly as tl
from scipy.linalg import sqrtm
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.utils.validation import check_is_fitted
from tensorly.decomposition import parafac

from cca_zoo.utils.check_values import _process_parameter, _check_views
from ._base import _BaseCCA


class TCCA(_BaseCCA):
    r"""
    Fits a Tensor CCA model. Tensor CCA maximises higher order correlations

    :Maths:

    .. math::

        \alpha_{opt}=\underset{\alpha}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \alpha_i^TK_i^TK_j\alpha_j  \}\\

        \text{subject to:}

        \alpha_i^TK_i^TK_i\alpha_i=1

    :Citation:

    Kim, Tae-Kyun, Shu-Fai Wong, and Roberto Cipolla. "Tensor canonical correlation analysis for action classification." 2007 IEEE Conference on Computer Vision and Pattern Recognition. IEEE, 2007
    https://github.com/rciszek/mdr_tcca

    :Example:

    >>> from cca_zoo.models import TCCA
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> X3 = rng.random((10,5))
    >>> model = TCCA()
    >>> model._fit((X1,X2,X3)).score((X1,X2,X3))
    array([1.14595755])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale=True,
        centre=True,
        copy_data=True,
        random_state=None,
        c: Union[Iterable[float], float] = None,
    ):
        """
        Constructor for TCCA

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, views will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param c: Iterable of regularisation parameters for each view (between 0:CCA and 1:PLS)
        """
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            accept_sparse=["csc", "csr"],
            random_state=random_state,
        )
        self.c = c

    def _check_params(self):
        self.c = _process_parameter("c", self.c, 0, self.n_views)

    def fit(self, views: Iterable[np.ndarray], y=None, **kwargs):
        """

        :param views: list/tuple of numpy arrays or array likes with the same number of rows (samples)
        """
        views = self._validate_inputs(views)
        self._check_params()
        # returns whitened views along with whitening matrices
        whitened_views, covs_invsqrt = self._setup_tensor(*views)
        # The idea here is to form a matrix with M dimensions one for each view where at index
        # M[p_i,p_j,p_k...] we have the sum over n samples of the product of the pth feature of the
        # ith, jth, kth view etc.
        for i, el in enumerate(whitened_views):
            # To achieve this we start with the first view so M is nxp.
            if i == 0:
                M = el
            # For the remaining views we expand their dimensions to match M i.e. nx1x...x1xp
            else:
                for _ in range(len(M.shape) - 1):
                    el = np.expand_dims(el, 1)
                # Then we perform an outer product by expanding the dimensionality of M and
                # outer product with the expanded el
                M = np.expand_dims(M, -1) @ el
        M = np.mean(M, 0)
        tl.set_backend("numpy")
        M_parafac = parafac(M, self.latent_dims, verbose=False)
        self.weights = [
            cov_invsqrt @ fac
            for i, (view, cov_invsqrt, fac) in enumerate(
                zip(whitened_views, covs_invsqrt, M_parafac.factors)
            )
        ]
        return self

    def correlations(self, views: Iterable[np.ndarray], **kwargs):
        """
        Predicts the correlation for the given data using the fit model

        :param views: list/tuple of numpy arrays or array likes with the same number of rows (samples)
        :param kwargs: any additional keyword arguments required by the given model
        """
        transformed_views = self.transform(views, **kwargs)
        transformed_views = [
            transformed_view - transformed_view.mean(axis=0)
            for transformed_view in transformed_views
        ]
        multiplied_views = np.stack(transformed_views, axis=0).prod(axis=0).sum(axis=0)
        norms = np.stack(
            [
                np.linalg.norm(transformed_view, axis=0)
                for transformed_view in transformed_views
            ],
            axis=0,
        ).prod(axis=0)
        corrs = multiplied_views / norms
        return corrs

    def score(self, views: Iterable[np.ndarray], **kwargs):
        """
        Returns the higher order correlations in each dimension

        :param views: list/tuple of numpy arrays or array likes with the same number of rows (samples)
        :param kwargs: any additional keyword arguments required by the given model
        """
        dim_corrs = self.correlations(views, **kwargs)
        return dim_corrs

    def _setup_tensor(self, *views: np.ndarray, **kwargs):
        train_views = self._centre_scale(views)
        n = train_views[0].shape[0]
        covs = [
            (1 - self.c[i]) * view.T @ view / (self.n)
            + self.c[i] * np.eye(view.shape[1])
            for i, view in enumerate(train_views)
        ]
        covs_invsqrt = [np.linalg.inv(sqrtm(cov)) for cov in covs]
        train_views = [
            train_view @ cov_invsqrt
            for train_view, cov_invsqrt in zip(train_views, covs_invsqrt)
        ]
        return train_views, covs_invsqrt


class KTCCA(TCCA):
    r"""
    Fits a Kernel Tensor CCA model. Tensor CCA maximises higher order correlations

    :Maths:

    .. math::

        \alpha_{opt}=\underset{\alpha}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \alpha_i^TK_i^TK_j\alpha_j  \}\\

        \text{subject to:}

        \alpha_i^TK_i^TK_i\alpha_i=1

    :Citation:

    Kim, Tae-Kyun, Shu-Fai Wong, and Roberto Cipolla. "Tensor canonical correlation analysis for action classification." 2007 IEEE Conference on Computer Vision and Pattern Recognition. IEEE, 2007

    :Example:

    >>> from cca_zoo.models import KTCCA
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> X3 = rng.random((10,5))
    >>> model = KTCCA()
    >>> model._fit((X1,X2,X3)).score((X1,X2,X3))
    array([1.69896269])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        eps=1e-3,
        c: Union[Iterable[float], float] = None,
        kernel: Iterable[Union[float, callable]] = None,
        gamma: Iterable[float] = None,
        degree: Iterable[float] = None,
        coef0: Iterable[float] = None,
        kernel_params: Iterable[dict] = None,
    ):
        """
        Constructor for TCCA

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, views will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param c: Iterable of regularisation parameters for each view (between 0:CCA and 1:PLS)
        :param kernel: Iterable of kernel mappings used internally. This parameter is directly passed to :class:`~sklearn.metrics.pairwise.pairwise_kernel`. If element of `kernel` is a string, it must be one of the metrics in `pairwise.PAIRWISE_KERNEL_FUNCTIONS`. Alternatively, if element of `kernel` is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two rows from views as input and return the corresponding kernel value as a single number. This means that callables from :mod:`sklearn.metrics.pairwise` are not allowed, as they operate on matrices, not single samples. Use the string identifying the kernel instead.
        :param gamma: Iterable of gamma parameters for the RBF, laplacian, polynomial, exponential chi2 and sigmoid kernels. Interpretation of the default value is left to the kernel; see the documentation for sklearn.metrics.pairwise. Ignored by other kernels.
        :param degree: Iterable of degree parameters of the polynomial kernel. Ignored by other kernels.
        :param coef0: Iterable of zero coefficients for polynomial and sigmoid kernels. Ignored by other kernels.
        :param kernel_params: Iterable of additional parameters (keyword arguments) for kernel function passed as callable object.
        :param eps: epsilon value to ensure stability
        """
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            random_state=random_state,
        )
        self.kernel_params = kernel_params
        self.gamma = gamma
        self.coef0 = coef0
        self.kernel = kernel
        self.degree = degree
        self.c = c
        self.eps = eps

    def _check_params(self):
        self.kernel = _process_parameter("kernel", self.kernel, "linear", self.n_views)
        self.gamma = _process_parameter("gamma", self.gamma, None, self.n_views)
        self.coef0 = _process_parameter("coef0", self.coef0, 1, self.n_views)
        self.degree = _process_parameter("degree", self.degree, 1, self.n_views)
        self.c = _process_parameter("c", self.c, 0, self.n_views)

    def _get_kernel(self, view, X, Y=None):
        if callable(self.kernel[view]):
            params = self.kernel_params[view] or {}
        else:
            params = {
                "gamma": self.gamma[view],
                "degree": self.degree[view],
                "coef0": self.coef0[view],
            }
        return pairwise_kernels(
            X, Y, metric=self.kernel[view], filter_params=True, **params
        )

    def _setup_tensor(self, *views: np.ndarray):
        self.train_views = views
        kernels = [self._get_kernel(i, view) for i, view in enumerate(self.train_views)]
        covs = [
            (1 - self.c[i]) * kernel @ kernel.T / (self.n - 1) + self.c[i] * kernel
            for i, kernel in enumerate(kernels)
        ]
        smallest_eigs = [
            min(0, np.linalg.eigvalsh(cov).min()) - self.eps for cov in covs
        ]
        covs = [
            cov - smallest_eig * np.eye(cov.shape[0])
            for cov, smallest_eig in zip(covs, smallest_eigs)
        ]
        self.covs_invsqrt = [np.linalg.inv(sqrtm(cov)).real for cov in covs]
        kernels = [
            kernel @ cov_invsqrt
            for kernel, cov_invsqrt in zip(kernels, self.covs_invsqrt)
        ]
        return kernels, self.covs_invsqrt

    def transform(self, views: np.ndarray, **kwargs):
        """
        Transforms data given a fit k=KCCA model

        :param views: list/tuple of numpy arrays or array likes with the same number of rows (samples)
        :param kwargs: any additional keyword arguments required by the given model
        """
        check_is_fitted(self, attributes=["weights"])
        views = _check_views(
            *views, copy=self.copy_data, accept_sparse=self.accept_sparse
        )
        views = self._centre_scale_transform(views)
        Ktest = [
            self._get_kernel(i, self.train_views[i], Y=view)
            for i, view in enumerate(views)
        ]
        transformed_views = [
            kernel.T @ self.weights[i] for i, kernel in enumerate(Ktest)
        ]
        return transformed_views
