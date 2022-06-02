# IMAGE FILTERING AND CODE SPEED

import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

path = "noisy_image.png"
im = np.asarray(Image.open(path))

plt.figure()
plt.imshow(im)
plt.show()