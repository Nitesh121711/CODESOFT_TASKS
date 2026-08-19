import os

password = "admin123"

user_input = input("Enter code: ")

eval(user_input)

os.system("ping " + user_input)

def login(username, password):
    if password == "admin123":
        return True
    return False