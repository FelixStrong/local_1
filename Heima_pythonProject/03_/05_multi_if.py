'''
print('Welcome to the zoo!')
# Height = int(input('tell me your height: '))
# VIP_Level = int(input("tell me your VIP level (1-5): "))

if int(input('tell me your height: ')) > 120:
    print('You are higher than 120 cm, you can''t visit the zoo for free.')
    print('But if your VIP level is higher than 3, it''s free.')
    if int(input("tell me your VIP level (1-5): ")) > 3:
        print('Your VIP Level is higher than 3, you can visit the zoo for free.')
    else:
        print('Your VIP level is lower than 3, you must pay 10 euros for ticket!')
else:
    print('Welcome, free')
print('have fun')
'''

print('Gift for collegues')
age = int(input('tell me your age: '))
if age > 18:
    print('You are older than 18, go on')
    if age < 30:
        print('You are between 18 and 30, go on')
        if int(input('How many years have you been working? ')) > 2:
            print('You can get gift from the company.')
        elif int(input('What is your Level? (1-5) ')) > 3:
            print('You can get gift from the company.')
        else:
            print('Sorry, no gift')
    else:
        print('You are too old, no gift')
else:
    print('You are too young, no gift')

