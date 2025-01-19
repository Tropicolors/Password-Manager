import random
import string
import json

data_file = "accounts.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def gen_password(length=12):
    passw = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(passw, k=length))

def add_account():
    service_name = input("Nom de la plateforme: ")
    email = input("Email utiliser: ")
    password = gen_password()
    data = load_data()
    if service_name not in data:
        data[service_name] = []
    data[service_name].append({"email": email, "password": password})
    save_data(data)
    print(f"Compte ajouter : Service: {service_name}, Email: {email}, Password: {password}")

def display_accounts():
    data = load_data()
    if not data:
        print("Pas de compte trouver.")
    else:
        print("Compte et passwords:")
        for service_name, accounts in data.items():
            print(f"Service: {service_name}")
            for account in accounts:
                if isinstance(account, dict) and 'email' in account and 'password' in account:
                    print(f"  Email: {account['email']}, Password: {account['password']}")
                else:
                    print("Données de compte mal formées.")


while True:
    print("Password Manager")
    print("1. Ajouter un compte")
    print("2. Afficher les comptes")
    print("3. Exit")
    choice = input("Sélectionnez une option: ")

    if choice == "1":
        add_account()
    elif choice == "2":
        display_accounts()
    elif choice == "3":
        break
    else:
        print("Erreur. Réessayer.")
