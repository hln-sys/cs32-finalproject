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

   # Grab the client's guess

        while True:
            client_guess = input('please input your hex guess: ')

            if len(client_guess) < 6:
                print('Hex guess must have 6 characters. Try again...')

            else:
                break

        s.sendall(client_guess)


        'the hex_code' = s.recv()


