# cs32-finalproject
HEXCODLE with Sylvia, Lena, and Hiranmayi

**Objective:**
The objective of this game is to create a color guesser game for interior designers, UI/UX designers, and color enthusiasts. There are two rounds, one where the player must guess the six digit hex code for the color and one where they can choose the color that they guessed correctly by moving and adjusting sliders. Initially, our READ.ME file suggested that we could guess the RGB values for the bonus round, but we changed this when we learned that we were required to include an element which we had not learned about in class. Instead of playing against a friend, we decided to include the element of a UI pop-up in our bonus round to fulfill this requirement. 

**Set up instructions:**
Use a MacBook
Download and use a local IDE, such as a VSCode
Connect your github account to access the files stored on github
In your terminal, run the following commands (without the quotation marks)
* ‘pip install hued’
* ‘pip install pillow’
* ‘pip install pygame’
* When you play, split your terminal.
 * In the first terminal, run server.py.
 * In the second terminal, run client.py.

**How our game works:**
On a broad level, it uses the smart client-dumb server format that we used in the Roshambo PSET to create and check hex code guesses that the client makes by using the ColorManager object and its conversion functions in the hued python library. The client also allows for a pop-up using the pygame library. 

<u> *A step-by-step run-down of our game* </u>
1. Using the Hued Python Library, generate a random color. Link: https://github.com/Infinitode/Hued
2. Using the Python Image Library, create and save an image to the files to the library.
3. Ask the user to check the files to open the picture of the color.
4. Then, using the smart client-dumb server format we made in the Roshambo PSET, ask the user to guess the color. Borrow the shim library socket32.py from the CS32 class.
5. Use a module that mimics Wordle to guess the six characters of the hex code game in six tries.
6. If the player guesses the hex code correctly, then implement a UI with the pygame library. For the next level, a pop-up will bring the user through an optional bonus round.
7. If the user clicks the ‘Yes’ button, they are shown a set of sliders which they can use to recreate the color they guessed from out.png. If they correctly slide the sliders, they win the bonus round. If they cannot pick the color with the sliders, they lose the bonus round and are told how far away from the correct color they are. Either way, the user can then click on the pop-up button and exit out of the game loop.
8. If the user clicks the ‘No’ button, they can click the pop-up and exit out of the game loop.

<u> *What each file does* </u>
* User Interface - This is a list of potential inputs and outputs that we created for the first FP submission
* Socket32 - A shim library that we borrowed from the CS 32 files that was used in Chapter 5’s lesson and in the Roshambo PSET. This allowed us to create a socket that connects two ports. We use this to connect our server and client.
* Server - Works along with client.py. Uses the Socket32 shim. Using the hued library, we generate and create a mystery hex code. This hex code is sent to the client. When the client stops sending messages to the server, the server terminates. 
* Client - Works along with server.py. Uses the Socket32 shim. First, it receives the mystery hex code from server.py. It then, inside a game loop, asks the user to input hex-code guesses and checks whether the guess is correct or not. Using the color coding from Wordle, the client prints to the terminal the guess that the user inputted, but with feedback on the placement of the hex characters. If the user guesses the hex code in six tries, they are given the chance to go to the bonus round. If not, the fact that the user has lost is printed to the terminal. Client has helper methods that create the UI and the buttons, as well as the sliders and distance formulate that are used to help run the bonus round. 
* Out - This is the file that stores the image that is generated each time the terminal runs server and client. 

**Sources:**
We used four main sources:
* Socket32.py, which is a shim library that we borrowed from CS32’s class files. It was created by the teaching staff of CS32 and is part of the cs50/cs32 files that we were able to get from the terminal. 
  * Documentation: https://cs50.readthedocs.io/cs50.dev/
* Chapter 05 class notes and code, PSET 3 code files, are the set of folders, files, and code that provided us a starter code structure for server.py and client.py. Many of the connection lines between server and client were borrowed from these files! These files were also written by the CS32 teaching staff and are part of the cs50/cs32 files that we got from the terminal.
  * Documentation: https://cs50.readthedocs.io/cs50.dev/
* Pygame library, which was originally written by Pete Shinners, in 2001.
  * We use it only in the client.py, and it is used to write 4 helper methods which are later called in our main function. These four helper methods help render the lines of text, show the bonus prompt, print desired messages of text, and show the sliders which we would need to click and drag to match the color in question. 
  * Here is the link: https://github.com/pygame
  * Documentation: https://www.pygame.org/docs/
* Hued library, which was created by the user Infinitode. As listed on their GitHub profile, Infinitode is “a cutting-edge small technology company dedicated to developing innovative solutions for the future of artificial intelligence, web development, and data science.” 
  * We use this library in both server.py and client.py. In client.py, we use it to perform conversions between rgb values, hex values, and hsv values. These are needed so that we can convert our slider values into rgb and hex values and vice versa for comparison. In server.py, we initialize and create a ColorManager object which lists all the possible hex code values we choose from. It also allows us to use conversion methods hex_to_rgb and rgb_to_hex, which we need for generating random values. Furthermore, in order to choose from a color on the ColorManager’s list, we also use the methods closest_color_name and get_color_by_name. 
  * Here is the link: https://github.com/Infinitode/Hued
  * We also used the documentation from this link: https://infinitode-docs.gitbook.io/documentation/package-documentation/hued-package-documentation/hued-reference
  * Infinitode’s page: https://github.com/Infinitode
* Artificial Intelligence
  * See note below.

**Generative AI Transparency Note:**
Our only use of AI was in client.py. Here, we used AI in order to help us write the code for the helper functions and the bonus round. AI wrote the import statements in lines 14, 15, and 16, wrote the helper functions render_text_lines(), show_bonus_prompt(), show_color_slider(), show_message(), and lines 227-252. These helper functions were related to UI and they:
* Showed the result message during the bonus round
* Showed the sliders during the bonus round
* Showed the buttons that make the bonus round optional
* Rendered multiple lines of text 
In addition, AI was also the one who was able to suggest which python libraries would be suited to creating a pop up and using a UI component in our work. AI also calculated Euclidean distance between two points in RGB. 

Below, I will paste the initial prompt to AI that we wrote to write the code we desired. We later kept exchanging prompts until we got the code and functionality that we wanted. 

*If the player guesses the words correctly, (inside the if statement if correct == 6), do the following statements. Create a UI interface pop up window that has the words “Do you want to play the bonus round?” Create two round buttons centered on the screen, one that says yes and is green, and one that says no and is red. The UI interface should have a white background. The words should be in Courier New. If the player clicks no, then write a pop up that says, return to the IDE. Break the game loop. If the player says yes, then show a visual slider or color wheel that the player can click on. Save the hex code that the player clicked on. If the hexcode matches the hexcode that was the secret code, then, the player wins the bonus round. Show the message “You won the bonus round” on the UI interface. If the player doesn’t click the right color on the color wheel or visual slider, calculate the distance from the color they clicked to the right color guess. Change the clicked hex code to RGB values. Use the RGB values of the correct hex code and the clicked hex code to find the Euclidean distance between the two colors. Show the message “You lost the bonus round. Your Euclidean distance from the correct color is (distance).” Then display the message “Return to the IDE” and break from the loop. Use the libraries Pygame, CustomTkinter, PyQt / PySide, and the Hued library already imported. For each new line of code, explain what you did. Do not drastically change the structure of our code. Only modify or add lines in between lines 68-70, and only complete the above instructions after the print statement completes. You can add import statements at the top of the code files, but please explain them as well. After completing the above instructions break out of the loop.*

**Limitations:**
Currently, our code is only able to work on MacOS. We do not have compatibility with Windows. We apologize for the inconvenience. 
