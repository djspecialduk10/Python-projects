import secrets
import string
import random

letters = string.ascii_letters
digits = string.digits
special = string.punctuation

characters = list(letters + digits + special)

def generate_password():
    password_length = int(input('How long do you want your password to be? '))

    random.shuffle(characters)

    password = []

    for pwd in range(password_length):
        password.append(random.choice(characters))

    
    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input('Do you want to generate a password? (Yes/No): ')

if option == 'Yes':
    generate_password()

elif option == 'No':
    print('program ended')
    quit()

else:
    print('Invalid input. Please enter Yes or No')
    quit()
