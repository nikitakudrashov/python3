from cryptography.fernet import Fernet
from main import load_key


key = load_key()
fernet = Fernet(key)



def authorization(login, password, fernet):
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            stored_login, stored_passwords = line.split("|")
            decrypted = fernet.decrypt(stored_passwords.encode()).decode()
            if login == stored_login and password == decrypted:
                return True
    return False

while True:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if authorization(login, password, fernet):
        print("Вы авторизованы")
        break
    else:
        print("Пользаватель не найден")
