from classes import *

import os

background = transform.scale(image.load(os.path.join(BASE_DIR, 'background.jpg')), (win_rez_x, win_rez_y))

player = Unit(os.path.join(BASE_DIR, 'x-wing.png'),
              win_rez_x / 2 - units_size / 2, win_rez_y * 7 / 8, units_size)