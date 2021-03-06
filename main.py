#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Due Jan 22, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Other Files
from global_variables import *
from classes import *
from level_design import *
from game import *
from menu import *

# Play intial music.
pygame.mixer.music.load(music_dict[current_music])
pygame.mixer.music.play(-1)

# Main function that calls the other main functions.
def main():
    global game_state
    global level_num

    # Create the two players
    Player0, Player1 = create_player_sprite(current_level) # returns a list of [Player0,Player1]

    # Main loop.
    running = True
    while running:

        # Capture events and check if user chose to close the program.
        events = pygame.event.get()
        for event in events:
            # If the user pressed to close the window then stop the program.
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        # Check if the user is in the menu or in game.

        # In the menu, call main_menu().
        if game_state == "menu":
            game_state, level_num = main_menu(events, level_num)

        # In the game, call main_game() and update json level if succeeded.
        elif game_state == "game":
            game_state, new_level = main_game(events, level_num, Player0, Player1)
            if new_level != level_num:
                level_num = new_level
                json_levels(True)

        # Not supposed to happen, quit to troubleshoot.
        else:
            running = False
            pygame.quit()


        # Refresh display.
        pygame.display.flip()

        # Make each frame stay for 50 miliseconds.
        clock.tick(50)

if __name__ == '__main__':
    main()
