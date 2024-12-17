import sys
import json
import requests
from style_task import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from requests import RequestException


API_URL = "https://dummyjson.com/products"

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.data = None

		self.setWindowTitle("Dummy API")
		self.setGeometry(100, 100, 400, 300)

		self.layout = QVBoxLayout()

		self.label = QLabel("Download json press button")
		self.fetch_btn = QPushButton("Fethc")
		self.save_btn = QPushButton("Save")

		self.layout.addWidget(self.label)
		self.layout.addWidget(self.fetch_btn)
		self.layout.addWidget(self.save_btn)

		self.fetch_btn.clicked.connect(self.fetch_data)
		self.save_btn.clicked.connect(self.save_date)

		self.setLayout(self.layout)

		self.show()


	def fetch_data(self):
		self.label.setText("Получаем данные с API...")
		self.data = self.get_data_from_api(API_URL)
		if self.data:
			self.label.setText("Данные получены успешно!")
		else:
			self.label.setText("Не удалось получить данные.")


	def save_date(self):
		if not self.data:
			print("No data")
			return
		
		options = QFileDialog.Option()
		file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "JSON Files (*.json);;All Files (*)", options=options)

		if file_name:
			self.save_to_file(self.data, file_name)
			self.show_message("Успех", f"Данные успешно сохранены в файл: {file_name}")

	def get_data_from_api(self, api_url):
		try:
			response = requests.get(api_url)

			response.raise_for_status()

			return response.json()
		except RequestException as e:
			print("Fetch error ", e)	
			return None

	def save_to_file(self, data, filename):
		try:
			with open(filename, "w", encoding="utf-8") as file:
				json.dump(data, file, ensure_ascii=False, indent=4)

				print("success saving")
		except IOError as e:
			print(e)

	def show_message(self, title, message):
			QMessageBox.information(self, title, message)			


def main():
	app = QApplication([])
	dummy = App()
	app.setStyleSheet(btn)

	sys.exit(app.exec_())

main()	