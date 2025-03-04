# Hyperspectral imaging (HSI)
Hyperspectral imaging (HSI) sensors are promising tools to monitor the energy budget and to control the heat and mass balance of the Arctic sea ice cover, as the surface reflectance of the sea ice is measured by HSI sensors. HSI sensors operate within a wavelength range and, depending on this range, reflectance is converted to broadband reflectance by retrieval algorithms. pectral resolution is an important characteristic of HSI, as the surface reflectance strongly depends on the wavelength. Also. incident and reflection angle controls the broadband reflectance of sea ice. Instrument characteristics and varying insolation caused by atmospheric particles and sky situations are two factors thatimpact HSI. In the NIR domain, the grain size of snow and ice plays a major role in the broadband reflectance and the BRDF of snow and sea ice is stronger in SWIR than in NIR.

The application of hyperspectral imaging has been widened in industry such as agriculture recently, and a variety of hyperspectral imaging sensors have been developed. Hyspex is a Norwegian brand for airborne and ground-based hyperspectral imaging. The spectral domain of Hyspex's cameras varies between 400-2500nm. Also, Specim is a Finnish company which offers a broadest range of hyperspectral cameras covering wavelengths in visible and NIR regions of electromagnetic spectrum. The specifications of some of Hyspex, BaySpec and Specim products are listed in the following table.

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

A digital color photograph is a combination of three colors, red, green, and blue, while a spectral image consists of dozens of channels. The portable and standalone hyperspectral camera, Specim-IQ, operates within the wavelength range between 400 and 1000 nm, including visible wavelength (400-700 nm) and NIR wavelength (700-1000 nm). The spatial resolution of the camera is 512×512 pixels (px), and the 204 channel bands make a high spectral resolution needed to analyze the surface reflectance of the sea ice.

The camera was designed based on push-broom technology, that is known as line scan hyperspectral camera. In this technology, spectral and spatial data of the sea ice surface are collected line by line, while whisk broom scanners capture the spectral information of a point on the measured object. In other words, the camera captures 512 lines of images and a square image (512×512 px) is obtained. The push broom instrument is more compact and lightweight compared to earlier whisk broom instruments. However, its calibration process is significantly more complex due to the increased number of detectors involved. In addition, snapshot hyperspectral imaging is a technique that captures hyperspectral images within a single integration period of a detector array, eliminating the need for scanning. Unlike pushbroom and whisk broom methods, this approach does not involve moving parts, minimizing the risk of motion-induced artifacts. Frame or snapshot imagers feature a more complex focal plane and exhibit slower read-out times, resulting in reduced imaging capacity compared to pushbroom scanners. However, they demonstrate a higher tolerance for significant rate knowledge errors and rate noise during image acquisition, while preserving overall image quality. During the MOSAiC campaign in July 2020, the camera recorded 651 data records in different sky and illumination conditions.

Basic data handling and data analysis processes, such as preprocessing and classification routines, are implemented within the camera software Specim IQ Studio and the Python programming language is used as a convenient interface for statistical and analytic purposes and for visualizing the data sets.

Capturing spatial and spectral parts of the Specim-IQ undergoes a slight temporal delay, causing distortions, if an object moves in the image. Also, vibrations create distortions during capturing the images. These vibrations impact the spatial image, while spectral signals are safe. Duration of measurement can be reduced, if fewer channel bands are chosen.
