# -*- coding: utf-8 -*-
"""q3.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XVSqQj0A74jh1tUjcXrA0oHgwzu0t44f
"""

import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image

img_url = 'https://www.greengold.tv/assets/Character/CB/Kalia.jpg'

with urllib.request.urlopen(img_url) as url:
    img = Image.open(url)
    img_array = np.array(img)

plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.imshow(img_array)
plt.axis('off')
# print("Original Image Array:\n", img_array)


rotated_img = np.rot90(img_array)

plt.subplot(1, 4, 2)
plt.imshow(rotated_img)
plt.axis('off')
plt.title("Rotated 90°")

flipped_img = np.fliplr(img_array)

plt.subplot(1, 4, 3)
plt.imshow(flipped_img)
plt.axis('off')
plt.title("Flipped Left-Right")

# Convert image to grayscale using the formula: Y = 0.299*R + 0.587*G + 0.114*B
gray_img = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])

# Plot grayscale image
plt.subplot(1, 4, 4)
plt.imshow(gray_img, cmap='gray')
plt.axis('off')
plt.title("Grayscale Image")

plt.tight_layout()
plt.show()