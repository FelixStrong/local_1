import random

num = random.randint(1, 10)
print('You have 3 chances to guess the random number')
guess_num = int(input('First try, guess the random number:'))
if guess_num == num:
    print('Perfect! First try is correct')
else:
    if guess_num < num:
        print('Too small')
    else:
        print('Too large')

    guess_num = int(input('Second try,  guess the random number:'))
    if guess_num == num:
        print('Good! Second try is correct')
    else:
        if guess_num < num:
            print('Too small')
        else:
            print('Too large')

        guess_num = int(input('Third try,  guess the random number:'))
        if guess_num == num:
                print('Not bad! Third try is correct')
        else:
            if guess_num < num:
                print('Too small')
            else:
                print('Too large')

            print('All your answer were wrong, the number is ' + str(num))


