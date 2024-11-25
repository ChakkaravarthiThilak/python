from PIL import Image
im=Image.open("C:/csc/sunset.jpg")
im.show()
a=(70,50,120,90)
crop=im.crop(a)
crop.show()


 
