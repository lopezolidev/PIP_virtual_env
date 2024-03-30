import random

# options = ('rock', 'paper', 'scissors')

# rounds = 0

# computer_wins = 0
# user_wins = 0

# while True:

#     print('*' * 10)
#     print('ROUND ', rounds)
#     print('computer ', computer_wins)
#     print('user ', user_wins)
#     print('*' * 10)

#     user_option = input("rock, paper, scissors → ").lower()
#     computer_option = random.choice(options)

#     rounds += 1

#     if not user_option in options:      # checking if the user took an invalid choice
#         print("That's not a valid choice!")
#         continue    # if we don't have a valid choice there's no need for the rest of the code to be executed

#     print("User's option -> ", user_option)
#     print("Computer's option -> ", computer_option)

#     if user_option == computer_option:
#         print("Draw!")
#     elif user_option == 'rock':
#         if computer_option == 'scissors':
#             print('rock beats scissors')
#             print('User wins!')
#             user_wins += 1
#         else:
#             print('paper beats rock')
#             print('Computer wins!')
#             computer_wins += 1
#     elif user_option == 'paper':
#         if computer_option == 'rock':
#             print('paper beats rock')
#             print('User wins!')
#             user_wins += 1
#         else:
#             print('scissors beats paper')
#             print('Computer wins!')
#             computer_wins += 1
#     elif user_option == 'scissors':
#         if computer_option == 'paper':
#             print('scissors beats paper')
#             print('User wins!')
#             user_wins += 1
#         else:
#             print('rock beats scissors')
#             print('Computer wins!')
#             computer_wins += 1
    
#     if computer_wins == 2:
#         print('Final winner is computer!')
#         break
#     if user_wins == 2:
#         print('Final winner is the user!')
#         break

# def select(player):
#     option = 0
#     if player == 'rock':
#         option = 1
#     elif player == 'paper':
#         option = 2
#     elif player == 'scissors':
#         option = 3
#     return option



def brawl(user, computer):
    return user - computer

def show_result(result):
    options = (1, 2, 3)
    user = int(input('Choose your weapon: 1. rock - 2. paper - 3. scissors → '))
    computer = random.choice(options)
    result = brawl(user, computer)
    return result
    
def play():
    user_wins = 0
    computer_wins = 0
    res = 0
    rounds = 0
    condition = True

    while condition:

        print('*' * 10)
        print('ROUND ', rounds)
        print('computer ', computer_wins)       # ← round-update message
        print('user ', user_wins)       
        print('*' * 10)

        if user_wins == 2:
            print('User wins this match!')
            condition = False  # updating the condition to stop the game
            continue
        elif computer_wins == 2:
            print('Computer wins this match!')
            condition = False
            continue

        res = show_result(res)
        if res == 0:
            print('DRAW!')
            continue
        elif res in {-2, 1}:
            user_wins += 1
            print('User wins this round!')
            continue
        elif res in {-1, 2}:
            computer_wins += 1
            print('Computer wins this round!')
            continue

play()
