from PIL import Image
im=Image.open("C:/csc/sunset.jpg")
im.show()
new=Image.open("C:/csc/sunset.jpg")
new.show()
position((im.width-new.width),(im.height-new.height))
im.paste(new,position)
im.show()

 
