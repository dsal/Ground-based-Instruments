"""
MIT License

Copyright (c) 2022 PolarRS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


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
from hscam import HSCam  # Ensure HSCam is defined or imported

class WRDetection:
    @staticmethod
    def get_wr_pos(file_path, number_of_cluster_pixels, show_image=False):
        hsc = HSCam(file_path)
        temp850 = hsc.datacube[:,:,130:140].mean(axis=2).copy()
        temp850_blurred = scipy.signal.convolve2d(temp850, np.ones((10,10))/100, mode="same")

        flat_indices = np.argpartition(temp850_blurred.flatten(), -number_of_cluster_pixels)[-number_of_cluster_pixels:]
        top_indices = flat_indices[np.argsort(-temp850_blurred.flatten()[flat_indices])]
        x, y = np.unravel_index(top_indices, temp850_blurred.shape)

        wr_x = np.sort(x)[len(np.sort(x)) // 2]
        wr_y = np.sort(y)[len(np.sort(y)) // 2]

        if show_image:
            plt.figure(figsize=(8, 8))
            plt.imshow(temp850_blurred.T, cmap="gray", vmin=0, vmax=1)
            plt.scatter(x, y, color='red', s=5, label='Cluster Pixels')
            plt.scatter(wr_x, wr_y, color='green', s=20, label='Middle Pixel')
            plt.legend()
            plt.title("Processed Image")

        return wr_y, wr_x
