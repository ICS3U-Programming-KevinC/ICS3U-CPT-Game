# !/user/bin/env python3
 
# Created by Kevin Csiffary
# Date: Jan. 11, 2023
# This program prints out Hello World! and my name

import ugame
import stage

# for the main game scene
def game_scene():
    # set the image bank on the pybadge
    image_bank_background = stage.Bank.from_bmp16("pain_background.bmp")

    # sets the size of the background grid to 10*8
    background = stage.Grid(image_bank_background, 10, 8)

    # displays the background and sets the frame rate to 60
    game = stage.Stage(ugame.display, 60)

    # sets the layers of the sprites
    game.layers = [background]

    # render all of the sprites
    game.render_block()

    while True:
        pass


if __name__ == "__main__":
    game_scene()
