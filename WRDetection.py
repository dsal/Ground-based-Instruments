"""
Algorithm Description:
An unsupervised algorithm has been designed to detect the pixel coordinates
of a white reference panel that serves as a Lambertian surface. The algorithm
operates under the assumption that the white reference panel exhibits the highest
reflectance within the field of view under given illumination conditions.

The white reference panel has to be the most reflective surface and the illumination
conditions are such that the panel's reflectance is maximized.

If some pixels outside the white reflectance panel reflects irradiance more strongly
than the white reference panel, the algorithm may erroneously identify this bright
surface as the white reference coordinates. This scenario can lead to incorrect detection,
especially in environments with highly reflective objects or surfaces such as overcast sky.

The algorithm scans the image to identify areas  with the highest reflectance values.
Then, based on the intensity of the reflectance, the algorithm determines the most likely
location of the white reference panel.
"""


# wrdetection.py
import numpy as np
import scipy.signal
import scipy.ndimage
import matplotlib.pyplot as plt
from HSCam import HSCam
from scipy.ndimage import binary_erosion

class WRDetection:
    def get_wr_pos(file_path, number_of_cluster_pixels, show_image=False):
        hsc = HSCam(file_path)
        temp850 = hsc.datacube[:,:,130:140].mean(axis=2).copy()
        temp850_blurred = scipy.signal.convolve2d(temp850, np.ones((10,10))/100, mode="same")
        img_normalized = (temp850_blurred - np.min(temp850_blurred)) / (np.max(temp850_blurred) - np.min(temp850_blurred))
        
        img_bin = np.where(img_normalized > 0.85, 1, 0).astype(np.uint8)
        img_eroded = binary_erosion(img_bin, structure=np.ones((15, 15))).astype(np.uint8)
        y_coords, x_coords = np.where(img_eroded == 1)
        lowest_x = np.min(x_coords)-15
        lowest_y = np.min(y_coords)-15

        flat_indices = np.argpartition(temp850_blurred.flatten(), -number_of_cluster_pixels)[-number_of_cluster_pixels:]
        top_indices = flat_indices[np.argsort(-temp850_blurred.flatten()[flat_indices])]
        x, y = np.unravel_index(top_indices, temp850_blurred.shape)

        wr_x = np.sort(x)[len(np.sort(x)) // 2]
        wr_y = np.sort(y)[len(np.sort(y)) // 2]

        if show_image:
            plt.figure(figsize=(6, 6))
            plt.imshow(temp850_blurred.T, cmap="gray", vmin=0, vmax=1)
            plt.scatter(x, y, color='red', s=5, label='Cluster Pixels')
            plt.scatter(wr_x, wr_y, color='green', s=20, label='Middle Pixel')
            plt.legend()
            plt.title("Processed Image")

            plt.figure(figsize=(6, 6))
            plt.imshow(img_eroded.T, cmap="gray", vmin=0, vmax=1)
            plt.plot([lowest_y, img_eroded.T.shape[1] - 1], [lowest_x, lowest_x], color='yellow', linewidth=1)
            plt.plot([lowest_y, lowest_y], [lowest_x, img_eroded.T.shape[0] - 1], color='yellow', linewidth=1)
            plt.legend()
            plt.axis('off')

        return wr_y, wr_x, lowest_y ,lowest_x