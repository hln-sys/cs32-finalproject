# cs32-finalproject
CS 32 Final Project Designer Game with Sylvia, Lena, and Hiranmayi


We are creating a color guesser game. There are two levels, one where the player must guess the six digit hex code for the color, and one where they guess the RGB values!

Step 0: Ask the user whether they want to play with against the computer or against a friend, and how many levels they want to try. (Not in our inputs/outputs yet.)

Playing against the computer!
1. Using the Hued Python Library, generate a random color. 
  Link: https://github.com/Infinitode/Hued
2. Using the Python Image Library, create and save an image to the files to the library.
3. Ask the user to check the files to open the picture of the color.
4. Then, using the smart client-dumb server format we made in the Roshambo PSET, ask the user to guess the color.
5. Use a module that mimics Wordle to guess the six characters of the hex code game in six tries.
6. For the next level, ask the user to guess the levels of red, green, and blue, like the number guesser game in class. (Not in our inputs/outputs yet.)

Playing against a friend!
Complete all steps as above, implementing the same format as the Roshambo PSET
Changes:
1. Generate the color via computer
2. Have the same code run on both the client and the server in order to facilitate two people playing against each other.
3. When one person finishes quicker than the other, a message is received on the other side, terminating the connection.
4. This indicates which player finished guessing the fastest and therefore is the winner.
