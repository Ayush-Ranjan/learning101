from PIL import Image
if __name__=='__main__':
    im = Image.open("robot.jpg")
    im.rotate(45).show()
