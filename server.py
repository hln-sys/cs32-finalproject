
''' The server generates a random color with its hex value. The color generated is then made into an image
and saved to a file that will be displayed to the client. The instructions to open this file are then sent to the client
so that they view it and make their guess.

'''

''' This script uses socket32.py, which is a shim that was created by the CS32 team at Harvard.
It also uses the HUED library, which has many color-related functions. 

'''

# Import the library that contains the colors and their hex values
from hued.conversions import hex_to_rgb, rgb_to_hex
from hued.colors import ColorManager
import random
from PIL import Image
from socket32 import create_new_socket

def generate_mystery_color():
    
     # Initialize the color manager object and the big list of colors
     color_master = ColorManager()

     # generate random values for r, g, and b
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)

     # use the randomly generated values to convert to a random hex value
     a_hex_color = rgb_to_hex(r, g, b)

     # use this to find the closest color with a name
     mystery_name = color_master.closest_color_name(a_hex_color)

     # use the name to generate all the information about that color, including its rgb and hex values
     mystery_color_info = color_master.get_color_by_name(mystery_name)

     # return this information, all enclosed in a dictionary
     return mystery_color_info
     

# Create a connection
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
            # Generate the random color, its image, its rgb value, and its hex value
            mystery_color = generate_random_color()

            # procure the hex_mystery value from the dictionary
            hex_mystery = mystery_color['Hex']

            # procure the rgb_mystery value from the dictionary
            rgb_mystery = mystery_color['RGB']

            # Generate the image from the rgb values returned
            sz = (100, 100)
            hex_image = Image.new('RGB', sz)
             
            # Create direct access to the pixels in the image
            pixels = hex_image.load() 
            
            # Set the color of each pixel 
            for x in range(size[0]):
               for y in range(size[1]):
                  pixels[x,y] = rgb_mystery    # assign each pixel to the value of the mystery color

            # show the image to the player
            hex_image.save('images/out.png')

            while True:   # message processing loop that checks for the guesses received
                client_guess = conn2client.recv()
                if client_guess == '':
                    break

                # send the hex mystery code to the smart client so they can carry out the checks
                else:
                    conn2client.sendall (hex_mystery)
            print('Disconnected')


if __name__ == '__main__':
    main()

