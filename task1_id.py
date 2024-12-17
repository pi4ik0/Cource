import requests
import json
from requests import RequestException

API_URL = "https://dummyjson.com/users"
OUTPUT_FILE = "users.json"

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()  # Возвращает словарь
    except RequestException as e:
        print("Fetch error:", e)
        return None

def save_to_file(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print("Data successfully saved to file.")
    except IOError as e:
        print("File write error:", e)

def main():
    print("Fetching users data...")
    data = fetch_data(API_URL)

    if data and "users" in data:  # Проверяем, что ключ 'users' существует
        users = data["users"]

        for user in users:
            print(f"ID: {user['id']}, Name: {user['firstName']} {user['lastName']}, Age: {user['age']}")

        save_to_file(users, OUTPUT_FILE)
    else:
        print("Error: Could not fetch users data.")

main()
