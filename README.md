# Hyperspectral imaging (HSI) in Polar Regions
by Ahmad Salehi

Hyperspectral imaging (HSI) sensors are powerful tools for environmental monitoring, resource management, and climate studies, where understanding surface reflectance and its interactions with energy is critical. HSI sensors operate within a wavelength range and, depending on this range, reflectance is converted to broadband reflectance by retrieval algorithms. Spectral resolution is an important characteristic of HSI, as the surface reflectance strongly depends on the wavelength. Also. incident and reflection angle controls the broadband reflectance of sea ice. Instrument characteristics and varying insolation caused by atmospheric particles and sky situations are two factors thatimpact HSI. In the NIR domain, the grain size of snow and ice plays a major role in the broadband reflectance and the BRDF of snow and sea ice is stronger in SWIR than in NIR.

The following video shows the surface reflectance of sea ice in a wavelength range 400-900 nm. The differences in images at these wavelengths are attributed to the higher reflectance of snow and sea ice surfaces in the visible region compared to the near-infrared (NIR) region. The bumpy surface is more obvious in the longer wavelengths because of the lower reflectance and reduced anisotropy effects in the NIR region. The white reference panel, designed to have a Lambertian surface with high reflectivity, appears bright in the entire video, serving as a standard reference to ensure accurate reflectance measurements. These observations highlight the importance of considering wavelength-dependent reflectance properties when analyzing hyperspectral data.

https://github.com/user-attachments/assets/38b4dcf5-46df-4671-8ed1-508efdd7e98b

A digital color photograph is a combination of three colors, red, green, and blue, while a spectral image consists of dozens of channels. The portable and standalone hyperspectral camera, Specim-IQ, operates within the wavelength range between 400 and 1000 nm, including visible wavelength (400-700 nm) and NIR wavelength (700-1000 nm). The spatial resolution of the camera is 512×512 pixels (px), and the 204 channel bands make a high spectral resolution needed to analyze the surface reflectance of the sea ice.

The camera was designed based on push-broom technology, that is known as line scan hyperspectral camera. In this technology, spectral and spatial data of the sea ice surface are collected line by line, while whisk broom scanners capture the spectral information of a point on the measured object. In other words, the camera captures 512 lines of images and a square image (512×512 px) is obtained. The push broom instrument is more compact and lightweight compared to earlier whisk broom instruments. However, its calibration process is significantly more complex due to the increased number of detectors involved. In addition, snapshot hyperspectral imaging is a technique that captures hyperspectral images within a single integration period of a detector array, eliminating the need for scanning. Unlike pushbroom and whisk broom methods, this approach does not involve moving parts, minimizing the risk of motion-induced artifacts. Frame or snapshot imagers feature a more complex focal plane and exhibit slower read-out times, resulting in reduced imaging capacity compared to pushbroom scanners. However, they demonstrate a higher tolerance for significant rate knowledge errors and rate noise during image acquisition, while preserving overall image quality. During the MOSAiC campaign in July 2020, the camera recorded 651 data records in different sky and illumination conditions.

![hsi at wavelength](https://github.com/user-attachments/assets/bfd58ee9-d85f-4ce8-b8e9-ea322fb6cf2e)

Basic data handling and data analysis processes, such as preprocessing and classification routines, are implemented within the camera software Specim IQ Studio and the Python programming language is used as a convenient interface for statistical and analytic purposes and for visualizing the data sets.

![25_hsi_basics_spectrum](https://github.com/user-attachments/assets/84b06598-0f4e-415f-9f0d-81e0b3da146b)
Figure 1: The number of channel bands covering wavelengths from 400 to 1000 nm.

![25_hsi_basics_vector_visualization](https://github.com/user-attachments/assets/408b353f-36ec-464a-ab85-aec798682309)
Figure 2: Vector visualization of Specim-IQ.

Capturing spatial and spectral parts of the Specim-IQ undergoes a slight temporal delay, causing distortions, if an object moves in the image. Also, vibrations create distortions during capturing the images. These vibrations impact the spatial image, while spectral signals are safe. Duration of measurement can be reduced, if fewer channel bands are chosen.

The application of hyperspectral imaging has been widened in industry such as agriculture recently, and a variety of hyperspectral imaging sensors have been developed. Hyspex is a Norwegian brand for airborne and ground-based hyperspectral imaging. The spectral domain of Hyspex's cameras varies between 400-2500nm. Also, Specim is a Finnish company which offers a broadest range of hyperspectral cameras covering wavelengths in visible and NIR regions of electromagnetic spectrum. The specifications of some of hyperspectral products are listed in the following tables.

| Brand | Product | Spatial Pixels | Spectral Range (nm) | Number of Channels | Spectral Resolution (nm) |
|----------------|-----|----------------|----------------|-----|-------------|
| Hyspex | Baldur V-1024 N | 1024 | 400-800/485-960/400-1000 | 72/88/106 | 5.5 |
| Hyspex | Mjolnir V-1240 | 1240 | 400–1000 | 200 | - |
| Hyspex | Mjolnir VS-620 & 1240 (V-1240) | 400–1000 (V-1240) | 200 (V-1240) | - |
| Hyspex | VNIR-1800 | 1800 | 400–1000 | 186 | 	3.26 |
| BaySpec | OCI-1000 | 2048 | 600-1000 | 100 | < 5 |
| BaySpec | OCI-2000 | 400x200 | 600-1000 | 20-25 | 12-15 |
| BaySpec | OCI-FL | 800 | 400-1000 | 60 | 10-12 |
| BaySpec | OCI-F | 800 | 400-1000 | 120 | 5-7 |
| BaySpec | OCI-F-HR | 800 | 400-1000 | 240 | 7 |
| Inno-Spec | GreenEye | - | 400-1000 | 80 | <7 |
| Inno-Spec | BlueEye | - | 220-380 | 80 | 2 |
| Specim | Specim-IQ | 512x512 | 400-1000 | 204 | 2.9 |

Table 1: HSI products operating in visible and NIR


| Brand | Product | Spatial Pixels | Spectral Range (nm) | Number of Channels | Spectral Resolution (nm) |
|----------------|-----|----------------|----------------|-----|-------------|
| Hyspex | Baldur S-640i N | 640 | 960-1675 | 208 | 3.36 |
| Hyspex | Baldur S-384 N | 384 | 960-2500 | 288 & 5.45 |
| Hyspex | Mjolnir S-620 | 620 | 970–2500 | 300 | - |
| Hyspex | Mjolnir VS-620 | 620 (S-620) | 970–2500 (S-620) | 300 (S-620) | - |
| Hyspex | SWIR-384 | 384 | 930-2500 | 288 | 5.45 |
| Hyspex | SWIR-640 | 640 | 960-2500 | 360 | 4.38 |
| EVK | Helios EC32 | 320 | 930-1700 | 248 | - |
| EVK | Helios EQ32 | 320 | 930-1700 | 248 | - |
| BaySpec | OCI-F-SWIR | 250 | 900-1700 | 80 | 10 |
| Surface Optics | 710-SWIR | 512 | 900-1700 | 288 | 2.78 |
| Inno-Spec | RedEye 1.7 | - | 950-1700 | 80 | 9 |
| Inno-Spec | RedEye 1.7 High Res | - | 950-1700 | 80 | 9 |
| Inno-Spec | RedEye 1.9 | - | 1100-1900 | 80 | 11 |
| Inno-Spec | RedEye 2.2 | - | 1200-2200 | 80 | 13 |
| Inno-Spec | RedEye 1.7 OEM | - | 950-1700 | 80 | 9 |
| Inno-Spec | BlackEye | - | 2900-4200 | 200 | 18 |
| Specim | Specim FX50 | - | 2700-5300 | 200 | - |
| Specim | Specim FX120 | - | 7700-12300 | 160 | 18 |

Table 2: HSI products operating in NIR and SWIR

## Download HSI Files
The dataset is derived from an experimental investigation employing spatially resolved hyperspectral imaging techniques to analyze Arctic sea ice. This dataset, accessible via the DOI link (https://doi.pangaea.de/10.1594/PANGAEA.939448), is hosted on PANGAEA, an open-access repository for earth and environmental science data. The following figure navigates you to download the data sets:

![Steps](https://github.com/user-attachments/assets/f4097ed5-7b58-499f-ac30-d072b32d1a8a)

In addition, you can download a sample file, as well as a CSV file containing features for the training and testing splits, from the 'Releases' section on the right panel of this repo.

# White Reference Detection
A white reference panel mounted on a tripod is placed horizontally during the hyperspectral imaging procedure, which is a Lambertian surface and uniformly reflects the sunlight in all directions. The panel is required to obtain relative reflectance in the image records. It is an approximation of a Lambertian reflector which is a surface property to scatter incident light in all directions. A rough surface scatters large parts of the incident light, which is the definition of diffuse reflection, and the remaining fraction is refracted and transmits in the medium according to Snell's law*, the refraction of incident light to a medium is controlled by refraction index of the medium. A rough surface is an optically inhomogeneous medium in which diffuse reflection occurs. Figure 3 shows the white reference panel used in a HSI measurement. The panel was installed on a stand to reflect the incident radiation to the hyperspectral camera. Also, the image illustrates the difference between the scattering of light by inhomogeneous and homogeneous mediums that illustrates the quality of the white reflectance panel and its ability to diffuse reflections by the white reflectance panel. The ability of the inhomogeneous surface to diffuse incident light is higher than that of the homogeneous surface, as the former is of a bumpy shape which reflects incident light with different angles, thus diffusing incident light.
[*According to Snell's law, the refraction of incident light to a medium is controlled by refraction index of the medium]

![RGB_hsi_043](https://github.com/user-attachments/assets/f3e66c66-03c3-4d26-bfaa-19290557d8f5)
Figure 3: This image shows the field of view in which the HSI measurements were carried out.

![Lambertian surface_enhanced](https://github.com/user-attachments/assets/fe6cad71-55f3-4518-a31b-30116e27b7fd)
Figure 4: a and b show specular and diffuse reflection at a rough surface of an optically homogeneous and inhomogeneous medium respectively.

White reference detection is a crucial preprocessing step. As hundreds of HSI images are analyzed, manual selection of a white reference requires tens of hours. In order to automatically detect it, an unsupervised method has been developed. This method can be used in HSI data sets in which the pixels with the highest relative reflectance belong to the white reference. In other words, if some pixels outside the white reference are the brightest pixels in reflectivity, this method is useless.

An unsupervised algorithm was designed to detect the pixel coordinates of a white reference panel that serves as a Lambertian surface. The algorithm operates under the assumption that the white reference panel exhibits the highest reflectance within the field of view under given illumination and atmospheric conditions. The white reference panel has to be the most reflective surface, and the illumination conditions are such that the panel's reflectance is maximized. If some pixels outside the white reference panel reflects irradiance more strongly than the white reference panel, the algorithm may erroneously identify this bright surface as the white reference coordinates. This scenario can lead to incorrect detection, especially in environments with highly reflective objects or surfaces such as overcast sky.

The algorithm scans the image to identify areas with the highest reflectance values. Then, based on the intensity of the reflectance, the algorithm determines the most likely location of the white reference panel.

![wr and rgb](https://github.com/user-attachments/assets/8cf2913d-6642-4e55-8da1-8529ae257226)
Figure 5: The right image is RGB and the left image is the output image of the white reference detection algorithm. The middle location of the red cluster is chosen as the white reference.

# Noise
Noise in hyperspectral imaging sensor includes thermal (Johnson) noise, quantization noise and shot (photon) noise each contributing to the corruption of spectral bands to varying degrees. These corrupted bands are often excluded from datasets to enhance the accuracy of subsequent analysis. Thermal motion of electrons inside conductors of the camera's electric sub-systems produces Johnson-Nyquist (or thermal) noise. Shot noise arises from the discrete nature of electric DC current and is related to the arrival of charge carriers at a specific place. Quantization noise is the distortion that occurs when an analog signal is converted into a digital signal with a limited number of discrete amplitudes. Quantization noise is the distortion introduced during the conversion of an analog signal to a digital signal with a limited number of discrete amplitudes. Shot noise in electronic devices originates from the quantized nature of electric charge and is a consequence of the random arrival of discrete charge carriers, such as electrons or holes, at a specific location. This stochastic process introduces fluctuations in the current, even under steady-state conditions, and is particularly significant in low-current or high-frequency applications.

Fixed Pattern Noise (FPN) is the spatial variation in pixel output values under uniform illumination. Pixel FPN is mainly due to the variation in the photodetector parameters and dark current. The following figure shows the impacts of FPN and its removal. The left image appears heavily distorted, making it difficult to see details in image. In contrast, the right image shows the same scene after the FPN has been removed. The background appears more uniform, with improved contrast and clarity. This correction improves image quality, making it easier to interpret and analyze thermal data.

![25_hsi_basics_fpn](https://github.com/user-attachments/assets/1f7cc454-e03a-4ba6-bfb5-de57578e489a)
Figure 6: An IR image with fixed pattern noise (left) and after the fixed pattern noise is removed (right).

![25_hsi_basics_noise_spectrum](https://github.com/user-attachments/assets/646d45ba-1ad0-47f8-837e-6b2c7dd44d6e)
Figure 7: These two figures show existence of low SNR beyond 850nm that contributes to fluctuations.

In addition to the fluctuations in the range 900-1000nm, there is an anomaly in most of the HSI images that is a substantial decrease in upper and lower pixels at longer wavelengths. The reason for this anomaly is still unknown; however, this darkening significantly impacts data processing such as the classification of sea ice surface properties and should be eliminated for further data analysis. The figure 7 shows the mentioned anomaly that corrupts pixels in NIR regions,, and the figure 6 demonstrates a data set without the corruption thathas onlyimpact of SNR (FPN).

![25_hsi_basics_low_snr](https://github.com/user-attachments/assets/e3a0fbbd-208a-4afe-85e9-53b2be3c8420)
Figure 8: These two figures show existence of low SNR beyond 850nm that contributes to fluctuations.

# Classification of Surface Types
The classification approach is used to obtain the surface-type fraction, along with their corresponding average reflectance spectra, by analyzing the entire set of measurements. This method enables the differentiation of various surface types, allowing for a comprehensive assessment of their spatial distribution and optical properties. By determining the proportions of each surface type and computing their characteristic reflectance, the approach provides valuable information on surface conditions, which can be used for further studies on ice dynamics, energy balance, and climate interactions.

In this repo., machine learning methods are employed to classify surface types using the Scikit-learn package. Specifically, logistic regression is utilized for pixel-based analysis, allowing the identification and differentiation of various ice surface categories based on their spectral characteristics. This approach enables efficient and automated classification by learning the relationships between input features and predefined surface types. Using logistic regression, the model assigns probabilities to each pixel, facilitating accurate categorization of sea ice features and improving the understanding of their spatial distribution.

An advantage of using hyperspectral camera data for classification is the ability to leverage the full spectral information available across multiple wavelength channels. Unlike RGB or multispectral imaging, which captures only a limited number of bands, hyperspectral imaging provides a continuous and detailed spectral profile for each pixel. In this study, each spectral channel serves as a distinct feature, enabling a more comprehensive characterization of the surface types. For example, if the dataset contains 170 spectral channels, each channel contributes unique information about the reflectance properties of different surface types, allowing for a more robust and accurate classification. This high-dimensional feature space improves the model’s ability to distinguish subtle spectral differences between ice, snow and melt ponds, improving classification precision. Furthermore, the richness of hyperspectral data reduces the risk of error in classification due to spectral overlap, making it particularly valuable for detailed surface-type discrimination in complex sea ice environments.

For the annotation process, GIMP and Adobe Photoshop are utilized to manually label the sea ice surface types. Each dataset consists of an image with a resolution of 512 × 512 pixels, which is imported into these software tools for annotation. To facilitate precise labeling, two separate layers are created, corresponding to the sea ice class and the melt pond class. Each annotated layer is then exported as an individual 512 × 512 pixels image, preserving the pixel-wise class information.

![image](https://github.com/user-attachments/assets/a92886ce-0c47-4ec6-a314-a5bfb303de2c)
Figure 9: Using GIMP software for annotation.

![image](https://github.com/user-attachments/assets/a5e3c3e9-38ef-4ee1-93eb-4c2c5abaf314)
Figure 10: Using Adobe Photoshop software for annotation.

![image](https://github.com/user-attachments/assets/fde3988f-c5da-45f7-8921-6fe4138e9f51)
Figure 11: The annotation process generates a 512×512 pixel image encoding both categorical and spatial information. Specifically, each annotated pixel is assigned a label (either red or magenta) and corresponding coordinates (y,x), representing its spatial position within the image.

The generated encoded image serves as input for constructing the feature dataframe, which is utilized for training and testing in classification tasks. This feature table is subsequently processed using Scikit-learn functions to facilitate model development and evaluation. By generating tens of these encoded images, we can produce hundreds of thousands of pixels, each serving as a row in the feature dataframe. This extensive dataset enables a more robust representation of the feature space, enhancing the effectiveness of classification models.

categorical and spatial information of labled pixels are derived through a pixel-wise labling process by leveraging the input images' RGBA values to identify specific regions associated with distinct surface types. The process can be described scientifically as follows:
1. Image Representation as a Numerical Array: the image is first converted into a NumPy array (image_array = np.array(image)). This transformation allows for efficient numerical operations and element-wise comparisons, which are necessary for classification tasks.
2. Definition of Target Colors in the RGBA Spectrum: two specific RGBA color values are predefined to represent different surface types. Pond color with with RGBA code [255, 0, 0, 255] corresponds to red with full opacity (alpha = 255), and sea ice color with RGBA code [255, 0, 255, 255] represents magenta (a combination of red and blue) with full opacity.
3. Binary Mask Generation for Classification: the np.all(image_array == pond_color, axis=-1) operation evaluates whether each pixel in the image exactly matches the RGBA value assigned to pond (i.e., [255, 0, 0, 255]). This results in a binary mask (binary_pond_array), where True denotes the presence of pond pixels and False denotes other regions. Similarly, np.all(image_array == seaice_color, axis=-1) generates another binary mask (binary_seaice_array) for identifying sea ice pixels in the image.

![13_4_saved_max](https://github.com/user-attachments/assets/cc47cefe-f537-499c-a081-d5cd808e71f8)
Figure 12: An example of a 512x512 encoded image with categorical and spatial information.

This approach enables the extraction of pixel coordinates associated with each class, ensuring accurate localization of sea ice and melt pond regions. The exported layer images are subsequently loaded into Python for further processing, where spectral features of each pixel are derived. These features include the relative reflectance values across 170 hyperspectral channels, spanning wavelengths from 400 nm to 900 nm. This pixel-wise feature extraction forms the basis for training the classification model, allowing for detailed spectral analysis and improved differentiation between sea ice and melt pond surfaces.

In this study, 86 hyperspectral datasets were used to extract spectral signatures for each pixel, with each pixel represented by 170 spectral channels. Each pixel is also assigned a class label, indicating whether it corresponds to sea ice or a melt pond, forming a binary classification problem. The final dataset consists of 303,169 pixels, each represented by a 170-dimensional feature vector alongside a categorical class label. This structured dataset is formatted into a dataframe, making it suitable for machine learning applications.

The large volume of data ensures statistical robustness, allowing models to learn distinguishing patterns between sea ice and melt ponds based on spectral properties. However, potential challenges such as class imbalance and spectral variability must be carefully addressed to ensure accurate classification. Given the high dimensionality of hyperspectral data, traditional machine learning models may suffer from the curse of dimensionality, where the increasing number of features leads to sparsity in the data space, reducing model generalization. Dimensionality reduction techniques such as Principal Component Analysis (PCA) or feature selection methods can be employed to mitigate these effects while preserving relevant spectral information. Additionally, class imbalance could affect the classification process, especially if one class (e.g., melt pond) is significantly overrepresented compared to the other (e.g., sea ice). In such cases, models may develop a bias toward the majority class, leading to poor detection of the minority class. Strategies such as resampling techniques, cost-sensitive learning, and balanced loss functions can be implemented to improve classification performance.

![Mean Comparison](https://github.com/user-attachments/assets/35143b5e-0acb-437b-a95b-9ac597155489)
Figure 12: Class imbalance in the classification of sea ice and melt ponds, represented by the unequal distribution of pixel frequencies between the two classes. The frequency corresponds to the total number of pixels assigned to each class (melt pond or sea ice).

Machine learning techniques such as Support Vector Machines (SVM), Random Forests, and Deep Learning-based Convolutional Neural Networks (CNNs) are commonly employed for hyperspectral image classification. These models can leverage the spectral characteristics of different materials to accurately differentiate between sea ice and melt ponds. Furthermore, given the continuous nature of hyperspectral data, spectral unmixing techniques or pixel-wise classification approaches can be applied to enhance accuracy. Feature engineering techniques, such as incorporating texture features or integrating spatial information, can further improve model performance. Proper validation strategies, including cross-validation and independent test set evaluation, are essential to ensure the reliability and generalizability of the developed classification models.

In the figure 13, the scatter plots depict the spectral relationships between the reflectance values of different hyperspectral channels for sea ice (blue) and melt pond (red). Each subplot represents a two-dimensional feature space, where the x-axis corresponds to the reflectance at 400 nm (Ch 0), and the y-axis corresponds to the reflectance at different wavelengths: 550 nm (Ch 50), 700 nm (Ch 101), 850 nm (Ch 152), and 900 nm (Ch 169).

![03  Scatters](https://github.com/user-attachments/assets/84d7d304-04a4-4e82-ac2b-ccb9fc3390b7)
Figure 13: Scatter plots illustrating the spectral relationships between Channel 0 (400 nm) and Channels 50 (550 nm), 101 (700 nm), 152 (850 nm), and 169 (900 nm). Data points are color-coded, with red representing melt ponds and blue representing sea ice.

From the scatter plots, it is evident that the spectral reflectance values of both classes exhibit strong correlation in certain channel combinations, particularly in the upper left plot (400 nm vs. 550 nm). The points align closely along a diagonal trend, indicating a high degree of linear correlation. In contrast, in the bottom right plot (400 nm vs. 900 nm), the spread of data points increases, suggesting a lower correlation between these spectral bands. The dispersion of melt pond pixels (red) is wider compared to sea ice pixels (blue), implying that melt ponds exhibit greater spectral variability in these wavelengths.

Correlation between features plays a crucial role in the robustness of machine learning models. Highly correlated features contribute redundant information, which may not enhance model learning significantly. Instead, they can lead to collinearity issues in linear models, increasing computational complexity without improving classification performance. However, when features exhibit moderate to low correlation, they provide complementary information, improving the model’s ability to generalize.

In the context of this dataset, strong correlations between spectral bands (as seen in the upper left scatter plot) suggest that these channels provide overlapping information. Feature selection techniques, such as Principal Component Analysis (PCA) or mutual information-based selection, can be used to reduce redundancy and improve model efficiency. On the other hand, the lower correlation in the bottom right plot indicates that additional spectral bands might contribute unique discriminatory information, enhancing the classifier's ability to distinguish between sea ice and melt ponds. If multiple features are highly correlated, machine learning models may overfit to redundant patterns, leading to inefficiencies in feature space representation. Dimensionality reduction techniques can mitigate this by removing redundant features while preserving the most informative ones. A diverse set of features with varying degrees of correlation contributes to a more robust model, allowing it to learn meaningful patterns beyond simple linear dependencies. This enhances the classifier's capability to generalize across unseen data. When features exhibit low or non-linear correlation, they can improve model performance by providing additional discrimination power. However, too many uncorrelated features can introduce noise, making it harder for the model to learn relevant patterns.

Performance of two classification algorithms, Random Forest (RF) and Logistic Regression (LR), was evaluated for predicting the pixel-wise class labels of a 512 × 512 hyperspectral image. RF required a considerably longer execution time, exceeding 19 minutes, to classify the entire HSI image. However, despite the computational burden, RF demonstrated robustness against class imbalance, yielding classification results that are well-aligned with the expected distribution of pixel classes. Compared to the reference RGB image, the classification output from RF remains reasonable, highlighting its ability to effectively capture complex spectral patterns and nonlinear decision boundaries. In contrast, LR exhibited a significantly shorter runtime of approximately 40 seconds. While its efficiency in terms of computation is advantageous for large-scale applications, the classifier struggled to accurately predict the class labels of hyperspectral pixels. LR does not inherently handle class imbalance, leading to biased predictions favoring the majority class and reduced classification accuracy for the minority class.

![RF_01_rgb](https://github.com/user-attachments/assets/e9950f6f-e8e3-47d1-baad-add0afd8e067)
Figure 14: The figure presents a classification map generated by a Random Forest (RF) algorithm, distinguishing between melt pond and sea ice.
