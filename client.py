''' The client receives an image from the server with the color.
The image is opened in a separate file and the client is directed to view it. After viewing, the client guess the hex value
of the image that has been displayed

The client has 6 guess chances '''

# NOTE: 1. Before beginning the game, Run 'pip install hued', 'pip install pillow', and 'pip install pygame' on your terminal to install the libraries needed for the game.
#       2. To make the guess once the game starts, you will be asked to check for an image in your files. The name of the file is 'out.png'
#          which will be created by the computer. Open it to see the image of the color whose hex value you have to guess.
#          This image changes everytime you have to make a new guess.

# Create a connection to the server
from socket32 import create_new_socket
import math  # use math.sqrt for Euclidean distance calculations
import pygame  # use Pygame for the UI windows and color selection
from hued.conversions import hex_to_rgb, rgb_to_hex, rgb_to_hsv, hsv_to_rgb

HOST = '127.0.0.1'
PORT = 65480

# UI helper function to render multiple lines of text in a Pygame window
def render_text_lines(surface, lines, font, color, start_x, start_y, line_spacing=4):
    y = start_y
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (start_x, y))
        y += text_surface.get_height() + line_spacing

# UI function that shows the buttons and displays the bonus prompt when the client clicks the right button
def show_bonus_prompt():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 22)
    screen = pygame.display.set_mode((520, 220))
    pygame.display.set_caption("Bonus Round")

    yes_rect = pygame.Rect(110, 100, 120, 60)
    no_rect = pygame.Rect(290, 100, 120, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'no'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if yes_rect.collidepoint(event.pos):
                    pygame.quit()
                    return 'yes'
                if no_rect.collidepoint(event.pos):
                    pygame.quit()
                    return 'no'

        screen.fill((255, 255, 255))
        label_surface = font.render("Do you want to play the bonus round?", True, (0, 0, 0))
        screen.blit(label_surface, label_surface.get_rect(center=(260, 50)))

        pygame.draw.ellipse(screen, (40, 167, 69), yes_rect)
        pygame.draw.ellipse(screen, (220, 53, 69), no_rect)
        yes_text = font.render("Yes", True, (255, 255, 255))
        no_text = font.render("No", True, (255, 255, 255))
        screen.blit(yes_text, yes_text.get_rect(center=yes_rect.center))
        screen.blit(no_text, no_text.get_rect(center=no_rect.center))

        pygame.display.flip()

# UI function for the bonus round that shows the color sliders (hue, saturation, value) 
def show_color_slider():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 18)
    screen = pygame.display.set_mode((760, 360))
    pygame.display.set_caption("Pick a Color")

    hue_rect = pygame.Rect(20, 90, 560, 30)
    sat_rect = pygame.Rect(20, 160, 560, 30)
    val_rect = pygame.Rect(20, 230, 560, 30)
    confirm_rect = pygame.Rect(320, 290, 120, 40)
    preview_rect = pygame.Rect(600, 100, 120, 120)

    hue = 0.0
    saturation = 1.0
    value = 1.0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hue_rect.collidepoint(event.pos):
                    hue = (event.pos[0] - hue_rect.left) / hue_rect.width
                elif sat_rect.collidepoint(event.pos):
                    saturation = (event.pos[0] - sat_rect.left) / sat_rect.width
                elif val_rect.collidepoint(event.pos):
                    value = (event.pos[0] - val_rect.left) / val_rect.width
                elif confirm_rect.collidepoint(event.pos):
                    rgb = hsv_to_rgb(hue * 360.0, saturation, value)
                    pygame.quit()
                    return rgb_to_hex(*rgb).lstrip('#').upper()
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if hue_rect.collidepoint(event.pos):
                    hue = (event.pos[0] - hue_rect.left) / hue_rect.width
                elif sat_rect.collidepoint(event.pos):
                    saturation = (event.pos[0] - sat_rect.left) / sat_rect.width
                elif val_rect.collidepoint(event.pos):
                    value = (event.pos[0] - val_rect.left) / val_rect.width
        
        hue = max(0.0, min(1.0, hue))
        saturation = max(0.0, min(1.0, saturation))
        value = max(0.0, min(1.0, value))

        screen.fill((255, 255, 255))
        render_text_lines(screen, [
            "Click and drag the sliders to choose hue, saturation, and value.",
            "Then click Confirm to save the selected color."
        ], font, (0, 0, 0), 20, 20)

        for x in range(hue_rect.width):
            color = hsv_to_rgb((x / hue_rect.width) * 360.0, 1, 1)
            pygame.draw.line(screen, color, (hue_rect.left + x, hue_rect.top), (hue_rect.left + x, hue_rect.bottom))
        pygame.draw.rect(screen, (0, 0, 0), hue_rect, 2)
        pygame.draw.circle(screen, (0, 0, 0), (hue_rect.left + int(hue * hue_rect.width), hue_rect.centery), 8, 2)
        screen.blit(font.render("Hue", True, (0, 0, 0)), (hue_rect.left, hue_rect.top - 25))

        for x in range(sat_rect.width):
            color = hsv_to_rgb(hue * 360.0, x / sat_rect.width, value)
            pygame.draw.line(screen, color, (sat_rect.left + x, sat_rect.top), (sat_rect.left + x, sat_rect.bottom))
        pygame.draw.rect(screen, (0, 0, 0), sat_rect, 2)
        pygame.draw.circle(screen, (0, 0, 0), (sat_rect.left + int(saturation * sat_rect.width), sat_rect.centery), 8, 2)
        screen.blit(font.render("Saturation", True, (0, 0, 0)), (sat_rect.left, sat_rect.top - 25))

        for x in range(val_rect.width):
            color = hsv_to_rgb(hue * 360.0, saturation, x / val_rect.width)
            pygame.draw.line(screen, color, (val_rect.left + x, val_rect.top), (val_rect.left + x, val_rect.bottom))
        pygame.draw.rect(screen, (0, 0, 0), val_rect, 2)
        pygame.draw.circle(screen, (0, 0, 0), (val_rect.left + int(value * val_rect.width), val_rect.centery), 8, 2)
        screen.blit(font.render("Value", True, (0, 0, 0)), (val_rect.left, val_rect.top - 25))

        selected_rgb = hsv_to_rgb(hue * 360.0, saturation, value)
        pygame.draw.rect(screen, selected_rgb, preview_rect)
        pygame.draw.rect(screen, (0, 0, 0), preview_rect, 2)
        
        pygame.draw.rect(screen, (40, 167, 69), confirm_rect)
        pygame.draw.rect(screen, (0, 0, 0), confirm_rect, 2)
        screen.blit(font.render("Confirm", True, (255, 255, 255)), (confirm_rect.left + 18, confirm_rect.top + 10))

        pygame.display.flip()

# UI function for the bonus round that shows the result message
def show_message(message_lines):
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 20)
    screen = pygame.display.set_mode((1400, 280))
    pygame.display.set_caption("Bonus Round Result")

    lines = message_lines if isinstance(message_lines, list) else [message_lines]
    lines.append("Return to the IDE by clicking this pop-up.")

    while True:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                pygame.quit()
                return

        screen.fill((255, 255, 255))
        render_text_lines(screen, lines, font, (0, 0, 0), 20, 20, line_spacing=8)
        pygame.display.flip()


def main():


    print('## Welcome to the HEXCODLE ! ##')

    print("Game Instructions:\n1. Before beginning the game, run 'pip install hued' on your terminal to install the hued library needed for the game.\nAlso run 'pip install pillow' and 'pip install pygame' on your terminal to install the image and game libraries needed, respectively.\n2. To make the guess once the game starts, you will be asked to check for an image in your files. The name of the file is 'out.png' which will be created by the computer. Open it to see the image of the color whose hex code you have to guess, excluding the hashtag (#). This image changes everytime you play a new game.\n3. Each guess must be a valid 6-character hex code and you have six tries. A valid Hex Code is a 6-character string containing only the characters 0-9 and A-F.\nWhen you make a guess you will be told how close you are to the true hex code by the colors of the character: \n   - A \033[32mgreen\033[0m character indicates that the character is in the hex code and in the correct spot \n   - A \033[33myellow\033[0m character indicates that the character is in the hex code but in the wrong spot \n   - A \033[90mgrey\033[0m character indicates that the character is not in the hexcode in any spot")


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

                player_guess = input('Please input your hex code guess: ').upper()

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

            print("#" + outcome)
            tries += 1

            if correct == 6:
                print(f"You got the correct hex code in {tries} tries!")
                play_choice = show_bonus_prompt()  # show the yes/no bonus round prompt

                if play_choice == 'no':
                    show_message("")  # show the return instruction in UI form
                    break  # break out of the game loop after the UI interaction

                if play_choice == 'yes':
                    clicked_hex = show_color_slider()  # show the color slider UI and save the selected hex

                    if not clicked_hex:
                        show_message("No color selected. Return to the IDE")  # show a cancellation message
                        break  # break the game loop on no color selection

                    correctly_guessed = clicked_hex == secret_choice.upper()  # compare the selected hex with the secret code
                    if correctly_guessed:
                        message_text = "You won the bonus round"
                    else:
                        correct_rgb = hex_to_rgb(secret_choice)  # convert the secret hex code to RGB using Hued
                        guessed_rgb = hex_to_rgb(clicked_hex)  # convert the clicked hex code to RGB using Hued
                        distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(correct_rgb, guessed_rgb)))  # compute Euclidean distance between the two colors
                        message_text = f"You lost the bonus round. Your Euclidean distance from the correct color is {distance:.2f}."

                    show_message(message_text)  # display the bonus round result
                    break

                break  # break out of the game loop after the bonus round completes

        if tries == 6 and correct != 6:
            print(f"You did not get the correct hex code in 6 tries! The correct hex code was: #{secret_choice}. Game over!")

if __name__ == '__main__':
    main()
