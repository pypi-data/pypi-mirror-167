
#cython: language_level=3

from cython.parallel cimport prange
from scipy.spatial.distance import cdist
import numpy as np
cimport numpy as np


def _distances(a, b, parallelize=False):
    r = np.zeros((a.shape[0], a.shape[1], b.shape[1]))
    if not parallelize:
        for i in range(a.shape[0]):
            r[i, :, :] = cdist(a[i, :, :], b[i, :, :])  # sklearn also has pairwise_distances
    else:
        raise AttributeError  # not implemented for now
        # for i in prange(a.shape[0], nogil=True):
        #     r[i, :, :] = cdist(a[i, :, :], b[i, :, :])
    return r

cdef _pairwise_distances(np.ndarray[np.float64_t, ndim=3] a, np.ndarray[np.float64_t, ndim=3] b):
    # Declarations
    cdef np.ndarray[np.float64_t, ndim=3] r
    cdef np.int32_t i, j, k

    r = np.zeros((a.shape[0], a.shape[1], b.shape[1]))

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(b.shape[1]):
                r[i, j, k] = np.sqrt(np.sum(np.square(a[i, j, :] - b[i, k, :])))

    return r


def pairwise_distances(a, b):
    return _pairwise_distances(a.astype('float64'), b.astype('float64'))  #


def _minimum_distances(a, b, box):
    # Convert box to right format
    box = box[:, np.newaxis, :]

    # Put a and b in box
    a = a - box * np.round(a / box)
    b = b - box * np.round(b / box)

    # Find minimum distances
    min_r = np.ones((a.shape[0], a.shape[1], b.shape[1])) * np.inf
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                # Move b
                bm = b + box * [dx, dy, dz]

                # Update min_r?
                r = _distances(a, bm)
                is_closer = r < min_r
                if np.sum(is_closer) > 0:
                    min_r[is_closer] = r[is_closer]

    # Return
    return min_r

def _minimum_cross_distances(a, box):
    # Convert box to right format
    box = box[:, np.newaxis, :]

    # Move `a` to origin
    ac = np.mean(a, axis=1)[:, np.newaxis, :]  # center of `a`
    a0 = a - box * np.round(ac / box)

    # Find minimum distances
    min_r = np.ones(a.shape[0]) * np.inf
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                # Skip origin
                if dx == 0 and dy == 0 and dz == 0:
                    continue

                # Move `a` to image
                am = a0 + box * [dx, dy, dz]

                # Update min_r?
                r = np.min(_pairwise_distances(a0, am), axis=(1, 2))
                is_closer = r < min_r
                if np.sum(is_closer) > 0:
                    min_r[is_closer] = r[is_closer]

    # Return
    return min_r