from PIL import Image
im=Image.open("C:/csc/sunset.jpg")
im.show()
rot=im.rotate(45,expand=True)
rot.show()


 
