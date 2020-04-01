from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
if __name__=='__main__':
    im=array(Image.open("apple.jpeg"))
    #imx=zeros(im.shape)
    #filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)
    #imy=zeros(im.shape)
    #filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
    im2=filters.gaussian_filter(im,5)
    im3=im/im2
    imshow(im3)
    show()
