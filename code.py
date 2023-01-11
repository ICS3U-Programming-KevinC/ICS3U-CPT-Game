# !/user/bin/env python3
 
# Created by Kevin Csiffary
# Date: Jan. 11, 2023
# This program prints out Hello World! and my name

import stage
import ugame

# for the main game scene
def game_scene():
    # set the image bank on the pybadge
    image_bank_background = stage.Bank.from_bmp16("pain_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("pain_sprites.bmp")

    # sets the size of the background grid to 10*8
    background = stage.Grid(image_bank_background, 10, 8)

    # sets the position of the 4 player sprites
    player1 = stage.Sprite(image_bank_sprites, 2, 67, 66)
    player2 = stage.Sprite(image_bank_sprites, 3, 67, 82)
    player3 = stage.Sprite(image_bank_sprites, 4, 83, 66)
    player4 = stage.Sprite(image_bank_sprites, 5, 83, 82)

    # sets player to all of the player sprites
    player = [player1] + [player2] + [player3] + [player4]

    # displays the background and sets the frame rate to 60
    game = stage.Stage(ugame.display, 60)

    # sets the layers of the sprites
    game.layers = [player] + [background]

    # render all of the sprites
    game.render_block()

    while True:
        # handle inputs
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("START")
        if keys & ugame.K_SELECT:
            print("SELECT")
        if keys & ugame.K_RIGHT:
            player.move(player.x + 1, player.y)
        if keys & ugame.K_LEFT:
            player.move(player.x - 1, player.y)
        if keys & ugame.K_UP:
            player.move(player.x, player.y - 1)
        if keys & ugame.K_DOWN:
            player.move(player.x, player.y + 1)      

        # renders the sprite every frame
        game.render_sprites([player])

        # only ticks every 1/60th of a second
        game.tick()


if __name__ == "__main__":
    game_scene()
