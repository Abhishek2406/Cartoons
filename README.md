# Cartoons
This is a project made with the help of OpenCV and numpy. The project takes an image as an input and makes a cartoon of the image and gives the image stack as output.
I have used a bilateral filter which reduces the colour palette which is necessary for the cartoon look and edge detection which allows production of bold silhouettes.
The image is converted to grayscale and median blur is applied to reduce the noise in the resultant grayscale image.
Using Adaptive Thresholding, an edge mask is created from the grayscale image so that the colour image and edge mask can be applied.

