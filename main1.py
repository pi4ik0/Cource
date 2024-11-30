import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QListWidget,
    QLineEdit, QInputDialog, QHBoxLayout, QVBoxLayout
)

# Ініціалізація застосунку
app = QApplication([])

# Дані нотаток
notes = {
    "Нотатка про json": {
        "текст": "Це приклад застосунку для нотаток на сайті.",
        "теги": ["добро", "інструкція"]
    }
}

# Збереження даних у файл
with open("notes_data.json", "w") as file:
    json.dump(notes, file)

# Створення інтерфейсу
notes_win = QWidget()
notes_win.setWindowTitle("Розумні нотатки")
notes_win.resize(800, 600)

# Віджети
list_notes = QListWidget()
list_notes_label = QLabel("Список нотаток")

button_note_create = QPushButton("Створити нотатку")
button_note_del = QPushButton("Видалити нотатку")
button_note_save = QPushButton("Зберегти нотатку")

field_tag = QLineEdit()
field_tag.setPlaceholderText("Введіть тег...")

button_tag_add = QPushButton("Додати до нотатки")
button_tag_del = QPushButton("Відкріпити від нотатки")
button_tag_search = QPushButton("Шукати нотатки за тегом")

list_tags = QListWidget()
list_tags_label = QLabel("Список тегів")

# Розміщення віджетів
layout_notes = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(list_notes_label)
col_1.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_1.addWidget(button_note_save)
col_1.addLayout(row_1)

col_2 = QVBoxLayout()
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_2 = QHBoxLayout()
row_2.addWidget(button_tag_add)
row_2.addWidget(button_tag_del)
row_2.addWidget(button_tag_search)
col_2.addLayout(row_2)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)

# Функції
def show_note():
    """Відображає вміст вибраної нотатки."""
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_tag.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])


# Підключення сигналів
list_notes.itemClicked.connect(show_note)

# Завантаження даних
with open("notes_data.json", "r") as file:
    notes = json.load(file)

list_notes.addItems(notes)

# Запуск застосунку
notes_win.show()
app.exec_()