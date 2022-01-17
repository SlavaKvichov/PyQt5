from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, \
    QVBoxLayout, QHBoxLayout, QPushButton, \
    QListWidget, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter, ImageOps


def save_image(image, image_name, operation):
    workdir = os.path.join(folderdir, 'Modified')
    if not os.path.isdir(workdir):
        os.mkdir(workdir)
    image.save(os.path.join(workdir, image_name.split('.')[0] + operation + image_name.split('.')[1]))
    return os.path.join(os.path.join(workdir, image_name.split('.')[0] + operation + image_name.split('.')[1]))


def copy_past():
    global filename
    try:
        filename = img_list.selectedItems()[0].text()
    except:
        filename = filelist[0]
    global img_dir
    img_dir = os.path.join(folderdir, filename)

def button_left_func():
    copy_past()
    with Image.open(img_dir) as file:
        rotate_img = file.transpose(Image.ROTATE_90)
    show_image(save_image(rotate_img, filename, 'rotateleft.'))


def button_right_func():
    copy_past()
    with Image.open(img_dir) as file:
        rotate_img = file.transpose(Image.ROTATE_270)
    show_image(save_image(rotate_img, filename, 'rotateright.'))


def button_mirror_func():
    copy_past()
    with Image.open(img_dir) as file:
        mirror_file = ImageOps.mirror(file)
    show_image(save_image(mirror_file, filename, 'mirror.'))


def button_blur_func():
    copy_past()
    with Image.open(img_dir) as file:
        blur_file = file.filter(ImageFilter.BLUR)
    show_image(save_image(blur_file, filename, 'blur.'))

def button_grey_func():
    copy_past()
    with Image.open(img_dir) as file:
        grey_image = file.convert('L')
    show_image(save_image(grey_image, filename, 'grey.'))



def img_list_func():
    file = img_list.selectedItems()[0].text()
    show_image(file)


def show_image(file):
    img.clear()
    image_path = os.path.join(folderdir, file)
    pixmapimage = QPixmap(image_path)
    with Image.open(image_path) as file:
        w, h = file.size[0], file.size[1]
        while True:
            if w > 800:
                w /= 1.05
                h /= 1.05
            else:
                break

    pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
    img.setPixmap(pixmapimage)
    img.show()


def folder_func():
    img_list.clear()
    global folderdir
    try:
        folderdir = QFileDialog.getExistingDirectory()
        filenames = os.listdir(folderdir)
        global filelist
        filelist = []
        for file in filenames:
            for req in REQUIRMENT:
                if file.endswith(req):
                    img_list.addItem(file)
                    filelist.append(file)
        try:
            show_image(filelist[0])
        except:
            img.setText('Папка пустая')
    except:
        pass


REQUIRMENT = ['jpg']


app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Easy Editor')

layout_h = QHBoxLayout()
main_win.setLayout(layout_h)

layout_v1 = QVBoxLayout()
layout_h.addLayout(layout_v1)
folder = QPushButton('Папка')
folder.clicked.connect(folder_func)
layout_v1.addWidget(folder)
img_list = QListWidget()
img_list.itemClicked.connect(img_list_func)
layout_v1.addWidget(img_list)

layout_v2 = QVBoxLayout()
layout_h.addLayout(layout_v2)
img = QLabel('Картинка')
layout_v2.addWidget(img, alignment=Qt.AlignLeft)
layout_v2_h = QHBoxLayout()
layout_v2.addLayout(layout_v2_h)
button_left = QPushButton('Лево')
button_left.clicked.connect(button_left_func)
layout_v2_h.addWidget(button_left)
button_right = QPushButton('Право')
button_right.clicked.connect(button_right_func)
layout_v2_h.addWidget(button_right)
button_mirror = QPushButton('Зеркально')
button_mirror.clicked.connect(button_mirror_func)
layout_v2_h.addWidget(button_mirror)
button_blur = QPushButton('Резкость')
button_blur.clicked.connect(button_blur_func)
layout_v2_h.addWidget(button_blur)
button_grey = QPushButton('Ч/Б')
button_grey.clicked.connect(button_grey_func)
layout_v2_h.addWidget(button_grey)

main_win.show()
app.exec_()