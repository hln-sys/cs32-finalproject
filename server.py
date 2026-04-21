
''' The server generates a random color with its hex value. The color generated is then made into an image
and saved to a file that will be displayed to the client. The instructions to open this file are then sent to the client
so that they view it and make their guess.

'''

# Import the library that contains the colors and their hex values
import HUED


# Create a connection
from socket32 import create_new_socket


HOST = '127.0.0.1'
PORT = 65489

def main():
     with create_new_socket() as s:
        # Bind socket to address and publish contact info
        s.bind(HOST, PORT)
        s.listen()
        print("HEXCODLE server started. Listening on", (HOST, PORT))

         # Answer incoming connection
        conn2client, addr = s.accept()
        print('Connected by', addr)

        with conn2client:
            # Generate the random color, it's image and it's hex value


            # Save the image generated in a file


            while True:   # message processing loop that checks for the guesses received
                client_guess = conn2client.recv()
                if client_guess == '':
                    break

                # send the image to the client so they can open it
                else:
                    conn2client.sendall ('the image')
            print('Disconnected')


if __name__ == '__main__':
    main()

