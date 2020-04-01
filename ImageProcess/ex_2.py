from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
if __name__=='__main__':
    im=array(Image.open("apple.jpeg"))
    im2=zeros(im.shape)
    im2=filters.gaussian_filter(im,5)
    im3=im-im2
    im4=im+im3	
    imshow(im4)
    show()
