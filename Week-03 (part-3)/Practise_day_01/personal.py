usernames = []
passwords = []
names = []


def register():
    names.append(input("Enter your name:"))
    usernames.append(input("choose your username:"))
    passwords.append(input("choose your password:"))


def login():
    username = input("Enter your username:")
    password = input("Enter your Password:")
    if username in usernames and password in passwords:
        print("welcome")
    else:
        print("incorrect!")


while True:
    account_ans = input("choose:  a)Sign Up     b)login and shop     c)quit ")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
    if account_ans == "c":
        break