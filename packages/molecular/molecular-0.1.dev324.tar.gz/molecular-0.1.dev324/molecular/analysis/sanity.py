
from molecular.analysis._analysis_utils import _minimum_cross_distances

from molecular.analysis import contacts, distances
from molecular.simulations import generate_images

import numpy as np


def has_cross_interactions(a, cutoff=4.5):
    # Move `a` to the origin
    am = a.to_origin(inplace=False)

    # Go through all images and find cross interactions
    is_crossed = np.zeros(a.n_structures, dtype='bool')
    for image in generate_images(exclude_origin=True):
        bm = a.to_image(*image, inplace=False)  # use `a` directly to avoid creating a copy
        is_crossed = is_crossed | np.max(contacts(am, bm, cutoff=cutoff, include_images=False), axis=(1, 2))

    # Return
    return is_crossed


def minimum_cross_distances(a):
    # # Move `a` to the origin
    # am = a.to_origin(inplace=False)
    #
    # # Go through all images and find cross interactions
    # distances = np.ones(a.n_structures) * np.inf
    # for image in generate_images(exclude_origin=True):
    #     bm = a.to_image(*image, inplace=False)  # use `a` directly to avoid creating a copy
    #     r = np.min(distances(am, bm, include_images=False), axis=(1, 2))
    #     mask = r < distances
    #     distances[mask] = r[mask]
    #
    # # Return
    # return distances

    # Extract coordinates
    a_xyz = a.xyz.to_numpy().reshape(*a.shape)

    # Extract boxes and check that `a_box` and `b_box` are identical
    box = a.box.to_numpy()

    # Finally, we can compute the minimum distances
    return _minimum_cross_distances(a_xyz, box)


