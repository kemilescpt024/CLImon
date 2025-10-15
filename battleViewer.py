import pygame
import os
from database import Dex
import threading

def display_battle_images(mon, opp):
    def pygame_loop():
        # Set window position before pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"  # x=100, y=100 on your screen

        pygame.init()
        screen_width, screen_height = 400, 200
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Battle View")

        bg_color = (245, 245, 245)
        screen.fill(bg_color)

        try:
            # Lookup Dex numbers
            imNumbMe = next((i for i, j in Dex.items() if j == mon.name), None)
            oppNumb = next((i for i, j in Dex.items() if j == opp.name), None)

            if imNumbMe is None or oppNumb is None:
                print("Could not find Pokémon in Dex.")
                return

            mon1_img = pygame.image.load(f"imageData/firered-leafgreen/back/{imNumbMe}.png")
            mon2_img = pygame.image.load(f"imageData/firered-leafgreen/{oppNumb}.png")

            mon1_img = pygame.transform.scale(mon1_img, (80, 80))
            mon2_img = pygame.transform.scale(mon2_img, (80, 80))

            screen.fill(bg_color)
            screen.blit(mon1_img, (40, 130))    # Left side
            screen.blit(mon2_img, (280, 60))   # Right side
            pygame.display.flip()

            # Event loop
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            pygame.quit()

        except Exception as e:
            print(f"Could not display images: {e}")

    threading.Thread(target=pygame_loop, daemon=True).start()
