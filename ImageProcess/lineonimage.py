from PIL import Image
from pylab import *
if __name__=='__main__':
    im=array(Image.open("robot.jpg"))
    imshow(im)
    x=[100,100,4000,4000]
    y=[200,3000,200,3000]
    plot(x,y,'ro')
    plot(x[:2],y[:2])
    title("Plotting:'empire.jpg'")
    show()