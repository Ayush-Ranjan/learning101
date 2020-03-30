from PIL import Image
from numpy import *
from scipy.ndimage import filters
if __name__=='__main__':
    im=array(Image.open("robot.jpg").convert("L"))
    im2=filters.gaussian_filter(im,5)