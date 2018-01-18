# How do you stop this loop?
'''
name=""
while name != 'your name':
    print('Please type your name: ')
    name=input()
print("Thank you")
'''

# using break() in a loop
'''
while True:
    print( "Please type your name")
    name = input()
    if name == 'your name':
        break
'''

# using continue() and break() to conrol a loop

while True:
    print("Enter your username: ")
    name = input()
    if name != "Joe":
        continue
    print("Hello Joe, What is the password?")
    password = input()
    if password == "swordfish":
        break
print("access granted")
