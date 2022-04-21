from time import sleep

def rps():
    import random
    global outplayed
    
    outplayed = 0
    player = '-1'
    
    while player != 'rock' or player != 'paper' or player != 'scissors':
        if player == 'rock' or player == 'Rock':
            value = 'Rock 🪨 '
            break
        elif player == 'paper' or player == 'Paper':
            value = 'Paper 🧻 '
            break
        elif player == 'scissors' or player == 'Scissors':
            value = 'Scissors ✂️ '
            break
        elif player == 'water' or player == 'Water':
            value = 'Water 🌊 '
            break
        elif player == 'imacheater':
            value = 0
            break
        else:
            if player == '-1':
                print('')
            else:
                print(f"\n{original} isn't any of the three.\nPlease choose between Rock, Paper or Scissors.\n")
            
            player = str(input('What do you want to play? '))
            original = player
    
    player = player[0].lower()

    if player == 'r':
        player = 1
    elif player == 'p':
        player = 2
    elif player == 's':
        player = 3
    
    r, p, s = 'Rock 🪨', 'Paper 🧻', 'Scissors ✂️'
    machine = random.choice([r,p,s])
    machineChoosed = machine

    machine = machine[0].lower()
    
    if machine == 'r':
        machine = 1
    elif machine == 'p':
        machine = 2
    elif machine == 's':
        machine = 3
    

    if machine == player:
        print(f"\nYou choose {value} | The computer choose {machineChoosed}\nIt's a drawn!\n\n")
    elif (machine == 1 and player == 2) or (machine == 2 and player == 3) or (machine == 3 and player == 1):
        print(f"\nYou choose {value} | The computer choose {machineChoosed}\nYou won! 😔\n\n")
    elif (machine == 1 and player == 3) or (machine == 2 and player == 1) or (machine == 3 and player == 2):
        print(f"\nYou choose {value} | The computer choose {machineChoosed}\nThe computer wins! 🎉\n\n")
    elif original == 'Water' or original == 'water':
        print(f'You choosed {value} and you broke the computer. GG!')
        outplayed = 1
    elif original == 'imacheater':
        print(f'YOU ARE A CHEATER!\n'*200)
        outplayed = 1

print(' ')
print(' ')
print('Welcome to Rock, Paper & Scissors')
print('Choose between Rock, Paper or Scissors to start playing!')
print('---------------------------------')

game = True

while True:
    if game == True:
        rps()
        game = False
        sleep(.8)
    elif outplayed == 1:
        break
    else:
        sleep(.2)
        response = str(input('Do you want to play again? (Y/N) '))
        if response == 'Y' or response == 'y':
            sleep(.8)
            rps()
        elif response == 'N' or response == 'n':
            game = False
            print('\nThanks for playing!\n')
            break
        else:
            print(f"{response} isn't a valid response.")
            sleep(.8)
        