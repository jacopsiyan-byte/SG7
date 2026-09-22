username = input("Enter username: ")

if 5 <= len(username) <= 10:
    if all(letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for letter in username):
        print("Valid username.")
    else:
        print("Invalid username.")
else:
    print("Invalid username.")