import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton \
    , QLabel, QListWidget, QLineEdit, QTextEdit \
        , QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

app = QApplication([])
notes = []

notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')
button_note_create = QPushButton('Створити замітку') 
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_search = QPushButton('Шукати замітки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)


def show_note():
	key = list_notes.selectedItems()[0].text()

	for note in notes:
		if note[0] == key:
			field_text.setText(note[1])
			list_tags.clear()
			list_tags.addItems(note[2])

def add_note():
	note_name, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки")

	if ok and note_name != "":
		note = [note_name, "", []]

		notes.append(note)

		list_notes.addItem(note[0])
		list_tags.clear()

		print(notes)

		with open(str(len(notes) - 1) + ".txt", "w") as file:
			file.write(note[0] + '\n')

def save_note():
	if list_notes.selectedItems():
		key = list_notes.selectedItems()[0].text()
		index = 0

		for note in notes:
			if note[0] == key:
				note[1] = field_text.toPlainText()

				with open(str(index) + ".txt", "w") as file:
					file.write(note[0] + "\n")
					file.write(note[1] + "\n")
					file.write(" ".join(note[2]))

			index += 1	

		print(notes)
	else:
		print("Error while saving")


def delete_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for index, note in enumerate(notes):
            if note[0] == key:
                notes.pop(index)
                list_notes.takeItem(list_notes.row(list_notes.selectedItems()[0]))

                filename = f"{index}.txt"
                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"File {filename} removed.")
                else:
                    print(f"File {filename} does not exist.")

                break
        print(notes)
    else:
        print("Error: Note not selected")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()

        if tag != "":
            for index, note in enumerate(notes):
                if note[0] == key:
                    if tag not in note[2]:
                        note[2].append(tag)
                        list_tags.addItem(tag)

                        with open(str(index) + ".txt", "w") as file:
                            file.write(note[0] + "\n")
                            file.write(note[1] + "\n")
                            file.write(" ".join(note[2]))

                        field_tag.clear()
                        break
        else:
            print("Tag is empty")
    else:
        print("Error while saving tag")

def delete_tag():
    if list_notes.selectedItems() and list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()

        for note in notes:
            if note[0] == key:
                if tag in note[2]:
                    note[2].remove(tag)
                    list_tags.clear()
                    list_tags.addItems(note[2])
                    break
        print(notes)
    else:
        print("Error: Either note or tag not selected")

def search_by_tag():
    tag = field_tag.text()
    if tag:
        matching_notes = [note[0] for note in notes if tag in note[2]]
        list_notes.clear()
        list_notes.addItems(matching_notes)
    else:
        print("No tag entered for search")


list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(delete_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(delete_tag)
button_tag_search.clicked.connect(search_by_tag)

notes_win.show()

name = 0 
note = []
while True:
	filename = str(name) + ".txt"

	try:
		with open(filename, "r") as file:
			note = file.readlines()
			note = [line.strip() for line in note]
			tags = note[2].split(" ")

			note[2] = tags

			notes.append(note)
			name += 1

	except IOError:
		break	

for note in notes:
	list_notes.addItem(note[0])


app.exec_()

