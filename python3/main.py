import os
import argparse
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

if not os.path.exists('key.key'):
    write_key()


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
    return key

key = load_key()
fernet = Fernet(key)


def add():
    name = input("Логин: ")
    password = input("Пароль: ")
    encrypt_password = fernet.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{encrypt_password}\n")
add()


def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            record = line.rstrip()
            login, password = record.split("|")
            decrypted_pass = fernet.decrypt(password.encode()).decode()
            print(f"Логин:{login} Пароль:{decrypted_pass}")
view()

while True:
    mode = input("Хотите добавить новый пароль или посмотреть уже существущие? 1 - посмотреть, 2 - добавить, 3 - выйти: ")
    if mode == "1":
        view()
    elif mode == "2":
        add()
    elif mode == "3":
        break
    else:
        print("Неверный выбор")
            

            


