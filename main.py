import random as r
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    code = " "

    for i in range(length):
        code += r.choice(characters)

    return code

length = int(input("Enter the password's Length : "))
password = generate_password(length)
print("Generated Password : ", password)