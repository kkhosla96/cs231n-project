# Automatic Colorization through Transfer Learning

This convolutional neural network model served as Kush and Cindy's final project for Stanford's CS 231N course (Spring 2018).

Given a grayscale image, our network performs automatic colorization using a fusion of an encoder decoder (Baldassare et al.) and hypercolumns from a VGG16 network (Dahl) pre-trained on ILSVRC 2012. Our model optimizes over the YCbCr colorspace and operates on square images. We utilized the L2 loss function as the primary evaluation for colorization accuracy.

Read our other experiments here: [LINK](https://github.com/kkhosla96/cs231n-project/files/2122564/final_paper.pdf)

### Architecture
![model](https://user-images.githubusercontent.com/21781041/41702148-e2f72c20-74e3-11e8-946d-ddb4d2d4826a.png)

### Depot Notes
Most of the work are in the project_vgg and project_encode_decode python notebooks. combine_plots and view_images are Python notebooks that make figures and run all our models on images, respectively. The python scripts are helper scripts that do mass directory reconstruction or file conversions.

### Data
This model has been tested on the 2018 COCO dataset. Data is not included in this repository, just due to size reasons.

### Performance
![samples](https://user-images.githubusercontent.com/21781041/41703922-c3806b4e-74e9-11e8-9ea4-c85a7926eb6d.png)

## Authors
- Kush Khosla (kkhosla at stanford.edu)
- Cindy Nguyen (cindyn at stanford.edu)

## References
**Deep Koalarization: Image Colorization using CNNs and Inception-ResNet-v2.** F. Baldassarre, D.G. Morín, L. Rodés-Guirao. In arXiv, 2017. [Article](https://arxiv.org/abs/1712.03400)

**Automatic Colorization** R. Dahl. 2016. [Article](http://tinyclouds.org/colorize/)

**Microsoft COCO: Common Objects in Context.** Lin et al. In Springer, 2016. [Article](https://arxiv.org/abs/1405.0312)


## Acknowledgments
- CS 231N Instructors
- Google Cloud Education Grant
