''' The client receives an image from the server with the color.
The image is opened in a separate file and the client is directed to view it. After viewing, the client guess the hex value
of the image that has been displayed

The client has 6 guess chances '''

# NOTE: 1. Before beginning the game, Run 'Pip install hued' on your terminal to install the hued library needed for the game
#       2. To make the guess once the game starts, you will be asked to check for an image in your files. The name of the file is 'out.png'
#          which will be created by the computer. Open it to see the image of the color whose hex value you have to guess.
#          This image changes everytime you have to make a new guess.

# Create a connection to the server
from socket32 import create_new_socket


HOST = '127.0.0.1'
PORT = 65489

def main():


    print('## Welcome to the HEXCODLE ! ##')

    #create socket and connect
    with create_new_socket() as s:
        s.connect(HOST, PORT)


# Grab the server choice:

secret_choice = s.recv()

# Grab player guess and compare with secret

while True:
    player_guess = input('Please input your hex code guess: ')

    if len(client_guess) == 6:
        break
    
    print('Your hex code guess must have 6 characters. Try again...')



# Check choice
while tries < 6:
    outcome = ""
    correct = 0
    tries = 0
    for i in range(len(player_guess)):
        # match - green
        if player_guess[i] == secret_choice[i]:
            outcome += f"\033[32m{player_guess[i]}\033[0m" 
            correct += 1
        elif player_guess[i] in secret_choice:
            outcome += f"\033[33m{player_guess[i]}\033[0m"
        else:
            outcome += f"{player_guess[i]}"
        tries += 1
    print(outcome)
    if correct == 6:
        print(f"You got the correct hex code in {tries}!")
        break

if tries == 6:
    print(f"You did not get the correct hex code in 6 tries! The correct hex code was: {secret_choice}. Game over!")



