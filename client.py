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
PORT = 65480

def main():


    print('## Welcome to the HEXCODLE ! ##')

    print("Game Instructions:\n1. Before beginning the game, Run 'pip install hued' on your terminal to install the hued library needed for the game.\n2. To make the guess once the game starts, you will be asked to check for an image in your files. The name of the file is 'out.png' which will be created by the computer. Open it to see the image of the color whose hex code you have to guess, excluding the hashtag (#). This image changes everytime you play a new game.\n3. Each guess must be a valid 6-character hex code and you have six tries. When you make a guess you will be told how close you are to the true hex code by the colors of the character: \n   - A \033[32mgreen\033[0m character indicates that the character is in the hex code and in the correct spot \n   - A \033[33myellow\033[0m character indicates that the character is in the hex code but in the wrong spot \n   - A \033[90mgrey\033[0m character indicates that the character is not in the hexcode in any spot")



    #create socket and connect
    with create_new_socket() as s:

        s.connect(HOST, PORT)

        # Grab the server choice:

        secret_choice = s.recv()

        tries = 0

        # Check choice
        while tries < 6:
            # Grab player guess and compare with secret
            outcome = ""

            correct = 0

            while True:

                player_guess = input('Please input your hex code guess: ').lower()

                if len(player_guess) == 6:
                    break

                print('Your hex code guess must have 6 characters. Try again...')

            for i in range(len(player_guess)):
                # match - green
                if player_guess[i] == secret_choice[i]:
                    outcome += f"\033[32m{player_guess[i]}\033[0m"
                    correct += 1
                # wrong spot - yellow
                elif player_guess[i] in secret_choice:
                    outcome += f"\033[33m{player_guess[i]}\033[0m"
                # wrong character - grey
                else:
                    outcome += f"\033[90m{player_guess[i]}\033[0m"
            print(outcome)
            tries += 1
            if correct == 6:
                print(f"You got the correct hex code in {tries} tries!")
                break

        if tries == 6:
            print(f"You did not get the correct hex code in 6 tries! The correct hex code was: {secret_choice}. Game over!")

if __name__ == '__main__':
    main()
