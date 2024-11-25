from PIL import Image
im=Image.open("C:/csc/sunset.jpg")
im.show()
flip=im.transpose(Image.ROTATE_180)
flip.show()

 
