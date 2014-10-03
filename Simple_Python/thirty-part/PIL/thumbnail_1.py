from PIL import Image
image = Image.open("wanted.jpg")
size=image.size
if size[0] > size[1]:
	rate = float(320) / float(size[0])
else:
	rate = float(180) / float(size[1])
new_size = (int(size[0]*rate),int(size[1]*rate))
new = image.resize(new_size, Image.BILINEAR)
new.save("1.jpg")
