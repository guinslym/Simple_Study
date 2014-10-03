from PIL import Image
image = Image.open("wanted.jpg")
width=320
height=320
image.thumbnail((width,height), Image.ANTIALIAS)
image.save("2.jpg")
