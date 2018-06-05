import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHI"
'''password = random.choice(chars)

print(password)
'''
password = ""
length = int(input("What's the password length that you want?"))
for i in range(length):
    for i in range(3):
        password += random.choice(chars)

    for i in range(3):
            if length in range(8):
                print("Your password is too weak")

    print(password)


