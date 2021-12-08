from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, \
    QVBoxLayout, QRadioButton, QHBoxLayout, QPushButton, QLabel, QButtonGroup
from random import shuffle


def show_question():
    button.setText('Ответить')                              # установить текст кнопки
    radio_group_box.show()                                  # показываем окно с вариантами вопросов
    answer_group_box.hide()                                 # прячем окно "Результаты теста"
    button_group_2.setExclusive(False)                      # снимает ограничения с кнопок
    qrbn1.setChecked(False)                                 # устанавливает статус нажатия как "False"
    qrbn2.setChecked(False)
    qrbn3.setChecked(False)
    qrbn4.setChecked(False)
    button_group_2.setExclusive(True)                       # возвращаем ограничения (если не сделать - можно нажать все кнопки)


def ask(ask_list):                                          # функция инициации вопросов
    show_question()
    question.setText(ask_list['вопрос'])
    shuffle(button_qroup)                                   # перемешивает кнопки
    button_qroup[0].setText(ask_list['правильный'])         # устанавливаем на случайную кнопку правильный вариант
    button_qroup[1].setText(ask_list['не правильный 1'])
    button_qroup[2].setText(ask_list['не правильный 2'])
    button_qroup[3].setText(ask_list['не правильный 3'])


def check_answer():
    radio_group_box.hide()                                  # прячет варианты ответа
    answer_group_box.show()                                 # показывает окно "результат теста"
    if button_qroup[0].isChecked():                         # проверяет, нажата ли кнопка с правильным ответом
        answer.setText('Правильно')
    else:
        answer.setText('Не правильно')
    button.setText('Следующий вопрос')


def button_ok():                                            # функция при нажатии на кнопку "Ответить"/"Следующий вопрос"
    if button.text() == 'Ответить':                         # если текст кнопки равен значению
        check_answer()
    else:
        next_question()


def next_question():                                        # переход к следующему вопросу
    main_win.current_question += 1
    if main_win.current_question == len(ask_list):          # если все вопросы уже были - начинаем с начала
        shuffle(ask_list)
        main_win.current_question = 0
    ask(ask_list[main_win.current_question])


app = QApplication([])                                      # создаём приложение

main_win = QWidget()                                        # создаем окно
main_win.current_question = 0                               # вводим переменную для отслеживания текущего вопроса
main_win.setWindowTitle('Memo Card')                        # задаём свойство объекта окно - заголовок

main_layout = QVBoxLayout()                                 # создаём вертикальную линию
main_win.setLayout(main_layout)                             # разпологаем вертикальную линию на окне

layout_H1 = QHBoxLayout()                                   # создаём горизонтальную линию
main_layout.addLayout(layout_H1)                            # распологаем горизонтальную линию на вертикальной
question = QLabel('Какой национальности не существует?')    # создаём объект текст
layout_H1.addWidget(question, alignment=Qt.AlignCenter)     # распологаем текст на горизонтальной линии, пытается держатся по центру(AlignCenter)

layout_H2 = QHBoxLayout()
main_layout.addLayout(layout_H2)
radio_group_box = QGroupBox('Варианты ответов:')            # создаём окошко с названием "Варианты ответов"
layout_H2.addWidget(radio_group_box)                        # распологаем её на горизонтальной линии
layout_H2_H1 = QHBoxLayout()
radio_group_box.setLayout(layout_H2_H1)
layout_H2_V1 = QVBoxLayout()
layout_H2_H1.addLayout(layout_H2_V1)
layout_H2_V2 = QVBoxLayout()
layout_H2_H1.addLayout(layout_H2_V2)
qrbn1 = QRadioButton('Энцы')                                # создаём кнопку
qrbn2 = QRadioButton('Чулымцы')
qrbn3 = QRadioButton('Смурфы')
qrbn4 = QRadioButton('Алеуты')
button_group_2 = QButtonGroup()                             # создаём объект "группа кнопок", нужна чтоб снять и поставить ограничения(можно нажать несколько вариантов)
button_group_2.addButton(qrbn1)                             # добавляем каждую кпоку в группу
button_group_2.addButton(qrbn2)
button_group_2.addButton(qrbn3)
button_group_2.addButton(qrbn4)
button_qroup = [qrbn1, qrbn2, qrbn3, qrbn4]                 # создаём список с кпонками для дальнеёшего их перемешивания
layout_H2_V1.addWidget(qrbn1)                               # распологаем кнопки на линиях внутри окошка "Варианты ответов"
layout_H2_V1.addWidget(qrbn3)
layout_H2_V2.addWidget(qrbn2)
layout_H2_V2.addWidget(qrbn4)
answer_group_box = QGroupBox('Результаты теста:')           # создаём еще одно окошко с названием "результаты теста"
layout_H2.addWidget(answer_group_box)                       # распологаем её на горизонтальной линии рядом с другим окошком "варианты ответов"
layout_H2_V3 = QVBoxLayout()
answer_group_box.setLayout(layout_H2_V3)
true_false = QLabel('Правильно/Неправильно')
layout_H2_V3.addWidget(true_false, alignment=Qt.AlignLeft)
answer = QLabel('Правильный ответ')
layout_H2_V3.addWidget(answer, alignment=Qt.AlignCenter)

layout_H3 = QHBoxLayout()                                   # создаём третюю горизонтальную линию
main_layout.addLayout(layout_H3)                            # распологаем её на нашей вертикальной
button = QPushButton('Ответить')                            # создаём кнопку "Ответить"
layout_H3.addWidget(button, alignment=Qt.AlignCenter)
button.clicked.connect(button_ok)                           # при нажатии на кнопку button срабатывает функция button_ok

ask_list = [                                                # список с вопросами
    {"вопрос": "Когда был 2000-ый год",
     "правильный": "в 2000-ом",
     "не правильный 1": "300 лет назад",
     "не правильный 2": "в рождение Исуса",
     "не правильный 3": "2 года назад"}
]
ask(ask_list[main_win.current_question])                    # инициирует программу - запуск первого вопроса

main_win.show()                                             # делаем чтоб окно было видно, по умолчанию стоит .hide (спрятать)
app.exec_()                                                 # пишем чтоб окно не закрывалось автоматически