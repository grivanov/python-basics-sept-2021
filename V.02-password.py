username = input()
password = input()

user_inp = input()

while user_inp != password:
    user_inp = input()

if user_inp == password:
    print(f"Welcome {username}!")
