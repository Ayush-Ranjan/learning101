from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
if __name__=='__main__':
    im=array(Image.open("square.jpg").convert('L'))
    imx=zeros(im.shape)
    filters.gaussian_filter(im, (5,5), (0,1), imx)
    imy=zeros(im.shape)
    filters.gaussian_filter(im, (5,5), (1,0), imy)
    im3=imx+imy
    imshow(im3)
    show()