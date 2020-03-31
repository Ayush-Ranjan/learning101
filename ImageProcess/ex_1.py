from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
if __name__=='__main__':
    im=array(Image.open("robot.jpg"))
    im2=zeros(im.shape)
    for i in range(3):
        im2[:,:,i]=filters.gaussian_filter(im[:,:,i],5)
        im2=uint8(im2)
    imshow(im)
    show()
