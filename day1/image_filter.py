# IMAGE FILTERING AND CODE SPEED

import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numba

path = "noisy_image.png"
im = np.asarray(Image.open(path))


filtered_im = np.zeros_like(im).astype(np.float64)


@numba.jit
def naive_image_filter(im, out):
    nr, nc = im.shape
    for r in range(nr):
        for c in range(nc):
            neighbors = 0
            value = 0
            for ro in range(-1, 2):
                r2 = r + ro
                if r2 >= 0 and r2 < nr:
                    for co in range(-1, 2):
                        c2 = c + co
                        if c2 >= 0 and c2 < nc:
                            neighbors += 1
                            value += im[r2, c2]
            out[r, c] = value / neighbors


weight_mask = np.ones_like(im) * 9
weight_mask[0] = 6
weight_mask[-1] = 6
weight_mask[:, 0] = 6
weight_mask[:, -1] = 6
weight_mask[0, 0] = 4
weight_mask[-1, 0] = 4
weight_mask[-1, -1] = 4
weight_mask[0, -1] = 4


def numpy_image_filer(im, out):
    out[:] = im  # CENTER

    out[:-1, :] += im[1:, :]  # RIGHT
    out[:-1, 1:] += im[1:, :-1]  # RIGHT  TOP
    out[:, 1:] += im[:, :-1]  # CENTER TOP
    out[1:, 1:] += im[:-1, :-1]  # LEFT TOP
    out[1:, :] += im[:-1, :]  # LEFT CENTER
    out[1:, :-1] += im[:-1, 1:]  # LEFT BOTTOM
    out[:, :-1] += im[:, 1:]  # CENTER BOTTOM
    out[:-1, :-1] += im[1:, 1:]
    out[:] /= weight_mask


naive_image_filter(im, filtered_im)
numpy_image_filer(im, filtered_im)
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
plt.imshow(im, cmap="gray")
ax = fig.add_subplot(1, 2, 2)
plt.imshow(filtered_im, cmap="gray")
plt.show()
