'''
print('Welcome to the zoo!')
Height = int(input('tell me your height: '))
VIP_Level = int(input("tell me your VIP level (1-5): "))

if Height < 120:
    print('You are under 120 cm, you can visit the zoo for free.')
elif VIP_Level > 3:
    print('Your VIP Level is higher than 3, you can visit the zoo for free.')
else:
    print('10 euros for tickt please')
print('have fun')
'''
'''

print('Let''s play a game!')
Number_1 = int(input('Think of a number (1-10): '))
Number_2 = int(input("Guess the number that i thought of: "))
if Number_2 != Number_1:
    Number_2 = int(input("It''s wrong, guess the number one more time: "))
    if Number_2 != Number_1:
        Number_2 = int(input("It''s wrong, guess the number at last: "))
        if Number_2 != Number_1:
            print('The Number is ' + str(Number_1))
'''
print('Let''s play a game!')
Number_1 = int(input('Think of a number (1-10): '))
if int(input("Guess the number that i thought of: ")) == Number_1:
    print('Perfect! First try!')
elif int(input("It''s wrong, guess the number one more time: ")) == Number_1:
    print("Good! Second try!")
elif int(input("It''s wrong, one last guess: ")) == Number_1:
    print("Not bad! Third try!")
else:
    print('傻逼！全错')
