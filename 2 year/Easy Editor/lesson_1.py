from PIL import Image, ImageFilter

with Image.open('4-38.jpg') as patrik:
    print(patrik.size)
    print(patrik.format)
    print(patrik.mode)
    bw_patrik = patrik.convert('L')
    mute_patrik = patrik.filter(ImageFilter.BLUR)
    rotate_patrik = patrik.transpose(Image.ROTATE_180)

    patrik.show()

    bw_patrik.show()
    mute_patrik.show()
    rotate_patrik.show()
