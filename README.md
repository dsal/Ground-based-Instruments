# Hyperspectral imaging (HSI)
Hyperspectral imaging (HSI) sensors are promising tools to monitor the energy budget and to control the heat and mass balance of the Arctic sea ice cover, as the surface reflectance of the sea ice is measured by HSI sensors. HSI sensors operate within a wavelength range and, depending on this range, reflectance is converted to broadband reflectance by retrieval algorithms. pectral resolution is an important characteristic of HSI, as the surface reflectance strongly depends on the wavelength. Also. incident and reflection angle controls the broadband reflectance of sea ice. Instrument characteristics and varying insolation caused by atmospheric particles and sky situations are two factors thatimpact HSI. In the NIR domain, the grain size of snow and ice plays a major role in the broadband reflectance and the BRDF of snow and sea ice is stronger in SWIR than in NIR.

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

A digital color photograph is a combination of three colors, red, green, and blue, while a spectral image consists of dozens of channels. The portable and standalone hyperspectral camera, Specim-IQ, operates within the wavelength range between 400 and 1000 nm, including visible wavelength (400-700 nm) and NIR wavelength (700-1000 nm). The spatial resolution of the camera is 512×512 pixels (px), and the 204 channel bands make a high spectral resolution needed to analyze the surface reflectance of the sea ice.

The camera was designed based on push-broom technology, that is known as line scan hyperspectral camera. In this technology, spectral and spatial data of the sea ice surface are collected line by line, while whisk broom scanners capture the spectral information of a point on the measured object. In other words, the camera captures 512 lines of images and a square image (512×512 px) is obtained. The push broom instrument is more compact and lightweight compared to earlier whisk broom instruments. However, its calibration process is significantly more complex due to the increased number of detectors involved. In addition, snapshot hyperspectral imaging is a technique that captures hyperspectral images within a single integration period of a detector array, eliminating the need for scanning. Unlike pushbroom and whisk broom methods, this approach does not involve moving parts, minimizing the risk of motion-induced artifacts. Frame or snapshot imagers feature a more complex focal plane and exhibit slower read-out times, resulting in reduced imaging capacity compared to pushbroom scanners. However, they demonstrate a higher tolerance for significant rate knowledge errors and rate noise during image acquisition, while preserving overall image quality. During the MOSAiC campaign in July 2020, the camera recorded 651 data records in different sky and illumination conditions.

Basic data handling and data analysis processes, such as preprocessing and classification routines, are implemented within the camera software Specim IQ Studio and the Python programming language is used as a convenient interface for statistical and analytic purposes and for visualizing the data sets.

![25_hsi_basics_spectrum](https://github.com/user-attachments/assets/84b06598-0f4e-415f-9f0d-81e0b3da146b)
Figure 1: The number of channel bands covering wavelengths from 400 to 1000 nm.

![25_hsi_basics_vector_visualization](https://github.com/user-attachments/assets/408b353f-36ec-464a-ab85-aec798682309)
Figure 2: Vector visualization of Specim-IQ.

Capturing spatial and spectral parts of the Specim-IQ undergoes a slight temporal delay, causing distortions, if an object moves in the image. Also, vibrations create distortions during capturing the images. These vibrations impact the spatial image, while spectral signals are safe. Duration of measurement can be reduced, if fewer channel bands are chosen.

# White Reference Detection
A white reference panel mounted on a tripod is placed horizontally during the hyperspectral imaging procedure, which is a Lambertian surface and uniformly reflects the sunlight in all directions. The panel is required to obtain relative reflectance in the image records. It is an approximation of a Lambertian reflector which is a surface property to scatter incident light in all directions. A rough surface scatters large parts of the incident light, which is the definition of diffuse reflection, and the remaining fraction is refracted and transmits in the medium according to Snell's law. A rough surface is an optically inhomogeneous medium in which diffuse reflection occurs. Figure \ref{fig:figures/28.png} shows the white reference panel used in HSI measurements during the MOSAiC campaign. The panel was installed on a stand to reflect the incident radiation to the hyperspectral camera in the MOSAiC expedition. Also, the image \ref{fig:figures/13.jpg} illustrates the difference between the scattering of light by inhomogeneous and homogeneous mediums \cite{lu2017light} that illustrates the quality of the white reflectance panel and its ability to diffuse reflections by the white reflectance panel. The ability of the inhomogeneous surface to diffuse incident light is higher than that of the homogeneous surface, as the former is of a bumpy shape which reflects incident light with different angles, thus diffusing incident light.\\
