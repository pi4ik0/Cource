import requests
import json

from requests import RequestException

API_URL = "https://dummyjson.com/products"
OUTPUT_FILE = "products.txt"

def fetch_data(api_url):
	try:
		response = requests.get(api_url)

		response.raise_for_status()

		return response.json()
	except RequestException as e:
		print("Fetch error ", e)	
		return None

def save_to_file(data, filename):
	try:
		with open(filename, "w", encoding="utf-8") as file:
			json.dump(data, file, ensure_ascii=False, indent=4)

			print("success saving")
	except IOError as e:
		print(e)


def main():
	print("GET product")

	data = fetch_data(API_URL)

	print(data)

	if data:
		print("200")
		save_to_file(data, OUTPUT_FILE)
	else:
		print("Error")	


main()