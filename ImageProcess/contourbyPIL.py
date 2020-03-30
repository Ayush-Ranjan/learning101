from PIL import Image
from pylab import*
if __name__=='__main__':
    im=array(Image.open("manface.jpeg").convert("L"))
    figure()
    gray()
    contour(im, origin="image")
    axis("equal")
    axis("off")