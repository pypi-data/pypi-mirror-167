# Copyright (c) 2020 Andrii Shekhovtsov

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method


class SPOTIS(MCDA_method):
    """ Stable Preference Ordering Towards Ideal Solution (SPOTIS) method.

        The SPOTIS method is based on an approach in which it evaluates given decision alternatives using the distance
        from the best ideal solution. [1].

        Read more in the :ref:`User Guide <SPOTIS>`.

        References
        ----------
        .. [1] Dezert, J., Tchamova, A., Han, D., & Tacnet, J. M. (2020, July). The SPOTIS rank reversal free method for
               multi-criteria decision-making support. In 2020 IEEE 23rd International Conference on Information Fusion
               (FUSION) (pp. 1-8). IEEE.

        Examples
        --------
        >>> from pymcdm.methods import SPOTIS
        >>> import numpy as np
        >>> body = SPOTIS()
        >>> matrix = np.array([[10.5, -3.1, 1.7],
        ...                    [-4.7, 0, 3.4],
        ...                    [8.1, 0.3, 1.3],
        ...                    [3.2, 7.3, -5.3]])
        >>> bounds = np.array([[-5, 12],
        ...                    [-6, 10],
        ...                    [-8, 5]], dtype=float)
        >>> weights = np.array([0.2, 0.3, 0.5])
        >>> types = np.array([1, -1, 1])
        >>> [round(preference, 4) for preference in body(matrix, weights, types, bounds)]
        [0.1989, 0.3705, 0.3063, 0.7491]
    """
    reverse_ranking = False

    def __init__(self):
        pass

    def __call__(self, matrix, weights, types, bounds, *args, **kwargs):
        """Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

            Parameters
            ----------
                matrix : ndarray
                    Decision matrix / alternatives data.
                    Alternatives are in rows and Criteria are in columns.

                weights : ndarray
                    Criteria weights. Sum of the weights should be 1. (e.g. sum(weights) == 1)

                types : ndarray
                    Array with definitions of criteria types:
                    1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.

                bounds : ndarray
                    Each row should contain min and max values for each criterion. Min and max should be different values!

                *args: is necessary for methods which reqiure some additional data.

                **kwargs: is necessary for methods which reqiure some additional data.

            Returns
            -------
                ndarray
                    Preference values for alternatives. Better alternatives have smaller values.
        """
        SPOTIS._validate_input_data(matrix, weights, types)
        if np.any(bounds[:, 0] == bounds[:, 1]):
            eq = np.arange(bounds.shape[0])[bounds[:, 0] == bounds[:, 1]]
            raise ValueError(
                    f'Bounds for criteria {eq} are equal. Consider changing min and max values for this criterion, '
                    f'delete this criterion or use another MCDA method.'
                )

        # Determine Ideal Solution Point based on criteria bounds
        isp = bounds[np.arange(bounds.shape[0]), ((types+1)//2).astype('int')]
        return SPOTIS._spotis(matrix, weights, isp, bounds)

    @staticmethod
    def _spotis(matrix, weights, isp, bounds):
        nmatrix = matrix.astype(float)
        # Normalized distances matrix (d_{ij})
        nmatrix = np.abs((nmatrix - isp)/
                         (bounds[:,0] - bounds[:,1]))
        # Distances to ISP (smaller means better alt)
        raw_scores = np.sum(nmatrix * weights, axis=1)
        return raw_scores

    @staticmethod
    def make_bounds(matrix):
        """ Returns bounds matrix for each criterion, e.g. extract min and max for each criterion values.

            Parameters
            ----------
                matrix : ndarray
                    Decision matrix.
                    Alternatives are in rows and Criteria are in columns.

            Returns
            -------
                bounds : ndarray
                    Min and max values (bounds) for each criterion.

            Examples
            --------
            >>> import numpy as np
            >>> from pymcdm.methods import SPOTIS
            >>> matrix = np.array([[ 96, 145, 200],
                                   [100, 145, 200],
                                   [120, 170,  80],
                                   [140, 180, 140],
                                   [100, 110,  30]])
            >>> types = np.ones(3)
            >>> weights = np.ones(3)/3
            >>> body = SPOTIS()
            >>> preferences = body(matrix, weights, types, bounds=bounds)
            >>> np.round(preferences, 4)
            array([0.5   , 0.4697, 0.4344, 0.1176, 0.9697])
            """
        return np.hstack((
            np.min(matrix, axis=0).reshape(-1, 1),
            np.max(matrix, axis=0).reshape(-1, 1)
        ))
