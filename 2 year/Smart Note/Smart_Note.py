from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, \
    QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QMessageBox
import json


def show_all_data():
    try:
        for i in data:
            list_notes.addItem(i)
            for j in data[i]['теги']:
                list_teg.addItem(j)
    except:
        pass


def show_note():
    try:
        list_teg.clear()
        key = list_notes.selectedItems()[0].text()
        text_field.setText(data[key]['текст'])
        for i in data[key]['теги']:
            list_teg.addItem(i)
    except:
        pass


def create_note_func():
    result = QInputDialog.getText(main_win, "Добавить заметку", "Название заметки:")[0]
    if result != '':
        data[result] = {
                'теги': [],
                'текст': ''
        }
        save_func()
        list_notes.clear()
        list_teg.clear()
        show_all_data()


def delete_note_func():
    try:
        key = list_notes.selectedItems()[0].text()
        data.pop(key)
        save_func()
        list_notes.clear()
        list_teg.clear()
        show_all_data()
    except:
        error = QMessageBox()
        error.setText('Выберете заметку, которую нужно удалить')
        error.exec()


def save_note_func():
    try:
        key = list_notes.selectedItems()[0].text()
        data[key]['текст'] = text_field.toPlainText()
        save_func()
    except:
        pass


def add_to_note_func():
    try:
        key = list_notes.selectedItems()[0].text()
        teg = teg_field.text()
        data[key]['теги'].append(teg)
        save_func()
        list_teg.addItem(teg)
    except:
        error = QMessageBox()
        error.setText('Выберете заметку, к которому добавить тег')
        error.exec()


def remove_from_note_func():
    try:
        key = list_notes.selectedItems()[0].text()
        teg = list_teg.selectedItems()[0].text()
        data[key]['теги'].remove(teg)
        save_func()
        list_notes.clear()
        list_teg.clear()
        show_all_data()
    except:
        error = QMessageBox()
        error.setText('Выберете заметку, с которой удалить тег')
        error.exec()


def search_by_teg_func():
    if search_by_teg.text() == 'Искать заметку по тегу':
        search_by_teg.setText('Сбросить поиск')
        teg = teg_field.text()
        list_notes.clear()
        for i in data:
            for j in data[i]['теги']:
                if teg == j or j.startswith(teg):
                    list_notes.addItem(i)
    else:
        list_notes.clear()
        list_teg.clear()
        show_all_data()
        search_by_teg.setText('Искать заметку по тегу')


def enter_func():
    global user_login
    user_login = login_login.text()
    user_password = login_password.text()
    if user_login in all_data and user_password == all_data[user_login]['password']:
        global data
        data = all_data[user_login]['data']
        save_func()
        login_win.hide()
        show_all_data()
        main_win.show()
    else:
        error = QMessageBox()
        error.setText('Логин или пароль не верный')
        error.exec()


def registration_func():
    global user_login
    user_login = login_login.text()
    user_password = login_password.text()
    if user_login not in all_data:
        all_data[user_login] = {
            'password': user_password,
            'data': {}
        }
        global data
        data = all_data[user_login]['data']
        save_func()
        login_win.hide()
        show_all_data()
        main_win.show()
    else:
        error = QMessageBox()
        error.setText('Этот логин уже занят')
        error.exec()


def save_func():
    all_data[user_login]['data'] = data
    with open('notes_data.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file)


try:
    with open('notes_data.json', 'r', encoding='utf-8') as file:
        all_data = json.load(file)
        print(all_data)
except:
    with open('notes_data.json', 'w', encoding='utf-8') as file:
        data = {}
        json.dump(data, file)
    with open('notes_data.json', 'r', encoding='utf-8') as file:
        all_data = json.load(file)
        print(all_data)

app = QApplication([])

main_win = QWidget()

layout_h = QHBoxLayout()
main_win.setLayout(layout_h)

text_field = QTextEdit()
layout_h.addWidget(text_field)
layout_v = QVBoxLayout()
layout_h.addLayout(layout_v)
list_notes_text = QLabel('Список заметок')
layout_v.addWidget(list_notes_text, alignment=Qt.AlignLeft)
list_notes = QListWidget()
layout_v.addWidget(list_notes)
layout_v_h = QHBoxLayout()
layout_v.addLayout(layout_v_h)
create_note = QPushButton('Создать заметку')
layout_v_h.addWidget(create_note)
delete_note = QPushButton('Удалить заметку')
layout_v_h.addWidget(delete_note)
save_note = QPushButton('Сохранить заметку')
layout_v.addWidget(save_note)
list_teg_text = QLabel('Список тегов')
layout_v.addWidget(list_teg_text, alignment=Qt.AlignLeft)
list_teg = QListWidget()
layout_v.addWidget(list_teg)
teg_field = QLineEdit()
layout_v.addWidget(teg_field)
teg_field.setPlaceholderText('Введите тег...')
layout_v_h2 = QHBoxLayout()
layout_v.addLayout(layout_v_h2)
add_to_note = QPushButton('Добавить к заметке')
layout_v_h2.addWidget(add_to_note)
remove_from_note = QPushButton('Открепить от заметки')
layout_v_h2.addWidget(remove_from_note)
search_by_teg = QPushButton('Искать заметку по тегу')
layout_v.addWidget(search_by_teg)
list_notes.itemClicked.connect(show_note)

create_note.clicked.connect(create_note_func)
delete_note.clicked.connect(delete_note_func)
save_note.clicked.connect(save_note_func)
add_to_note.clicked.connect(add_to_note_func)
remove_from_note.clicked.connect(remove_from_note_func)
search_by_teg.clicked.connect(search_by_teg_func)

login_win = QWidget()
login_layout = QVBoxLayout()
login_win.setLayout(login_layout)
login_text = QLabel('Введите логин и пароль')
login_layout.addWidget(login_text)
login_login = QLineEdit()
login_layout.addWidget(login_login)
login_login.setPlaceholderText('Логин')
login_password = QLineEdit()
login_layout.addWidget(login_password)
login_password.setPlaceholderText('Пароль')
login_h_layout = QHBoxLayout()
login_layout.addLayout(login_h_layout)
enter = QPushButton('Войти')
login_h_layout.addWidget(enter)
registration = QPushButton('Зарегистрировать')
login_h_layout.addWidget(registration)

enter.clicked.connect(enter_func)
registration.clicked.connect(registration_func)

login_win.show()

app.exec_()