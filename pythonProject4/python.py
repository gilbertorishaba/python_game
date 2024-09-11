# import random
# playing = True
# while playing:
#     choice = input('Roll the dice?(y/n):').lower()
# if choice1 == 'y':
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     print(f'{dice1}, {dice2}')
# elif choice1 == 'n':
#     print('Thanks for playing')
#     break
# else:
#     print('invalid choice')
import random

# import random
#
# guess_number = random.randint(1, 100)
#
# try:
#     your_guess = int(input('guess a number between 1 and 100:'))
#     if guess_number < your_guess:
#         print('To low!')
#     elif guess_number > your_guess:
#         print('To high!')
#     else:
#         print('Congratulations! You guessed the number')
#
# except valueError:
#     print('please enter a valid number')

import random

# using  if and elif
# if user_input == 'r':
#     print('👌')
# elif user_input == 'p':
#     print('🎶')
# else:
#     print('❤️')
# if user_input != r and user_input != p and user_input != s:

user_input = input('Rock, paper, scissors(r/s/p)')
choices = ('r', 's', 'p')
# using a data dictionary to manage the key value pairs
emoji = {'r': '👌', 's': '🎶', 'p': '❤️'}

if user_input not in choices:
    print('invalid choice')

computer_choice = random.choice(choices)

print(f'you chose {emoji[user_input]}')
print(f'Computer chose {emoji[computer_choice]}')

if user_input == computer_choice:
    print('Tie!')
elif user_input == computer_choice or \
        user_input == 'r' and computer_choice == 's' or \
        user_input == 's' and computer_choice == 'p':
    print('You win')
else:
    print('You loose')
