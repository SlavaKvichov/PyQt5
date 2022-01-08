from PIL import Image, ImageFilter, ImageOps

with Image.open('owl.jpg') as owl:
    print(owl.size)
    print(owl.format)
    print(owl.mode)
    owl.show()
    grey_owl = owl.convert('L')
    grey_owl.save('grey_owl.jpg')
    grey_owl.show()
    mute_owl = owl.filter(ImageFilter.BLUR)
    mute_owl.show()
    rotate_owl = owl.transpose(Image.ROTATE_90)
    rotate_owl.show()
    mirror_owl = ImageOps.mirror(owl)
    mirror_owl.show()