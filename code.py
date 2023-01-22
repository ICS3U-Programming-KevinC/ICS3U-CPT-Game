# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Jan. 11, 2023
# This program is my game


import stage
import ugame
import time
import random
import supervisor

import constants



def splash_screen():
    game = stage.Stage(ugame.display, 60)
    # set the image bank on the pybadge
    for i in range(5):
        slice_bmp = stage.Bank.from_bmp16(f"slice{i}.bmp")
        cur_slice = stage.Grid(slice_bmp, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
        for y in range(16):
            if y >= 8:
                c = 1
            else:
                c = 0
            cur_slice.tile((i * 2) + c, y - (8 * c), y)
        game.layers += [cur_slice]


    # render all of the sprites
    game.render_block()

    while True:
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("pain_menu.bmp")

    text = []
    text1 = stage.Text(width=40, height=20, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(59, 20)
    text1.text("Pain")
    text.append(text1)

    text5 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text5.move(15, 45)
    text5.text("Press A to Shoot")
    text.append(text5)

    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(5, 65)
    text3.text("Move Left and Right")
    text.append(text3)

    text4 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text4.move(25, 75)
    text4.text("With the Left")
    text.append(text4)

    text6 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text6.move(13, 85)
    text6.text("and Right Buttons")
    text.append(text6)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(4, 110)
    text2.text("Press Start To Play")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background, 10, 8)

    back_music = open("white_space.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    game = stage.Stage(ugame.display, 60)

    # sets the layers of the sprites
    game.layers = text + [background]

    # render all of the sprites
    game.render_block()
    sound.play(back_music)

    back_music_time = 0

    while True:
        # handle inputs
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START:
            game_scene()

        if back_music_time >= 838:
            sound.play(back_music)
            back_music_time = 0
        else:
            back_music_time += 1

        # only ticks every 1/60th of a second
        game.tick()

# for the main game scene
def game_scene():

    def show_enemy():
        for enemy_number in range(len(enemys)):
            if enemys[enemy_number].x < 0: 
                enemys[enemy_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    score = 0

    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text(f"Score: {score}")

    # set the image bank on the pybadge
    image_bank_background = stage.Bank.from_bmp16("pain_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("pain_sprites.bmp")


    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]



    # sets the size of the background grid to 10*8
    background = stage.Grid(image_bank_background, 10, 8)

    # sets the position of the 4 player sprites
    player1 = stage.Sprite(image_bank_sprites, 2, 67, 98)
    player2 = stage.Sprite(image_bank_sprites, 3, 67, 114)
    player3 = stage.Sprite(image_bank_sprites, 4, 83, 98)
    player4 = stage.Sprite(image_bank_sprites, 5, 83, 114)


    enemys = []
    for enemy_number in range(constants.TOTAL_NUMBER_OF_ENEMYS):
        a_single_enemy1 = stage.Sprite(image_bank_sprites, 7, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        #a_single_enemy2 = stage.Sprite(image_bank_sprites, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y - 16)
        enemys.append(a_single_enemy1)
        #enemys.append(a_single_enemy2)
    show_enemy()

    hit_sound = open("hit_sound.wav", 'rb')
    pew_sound = open("throw.wav", 'rb')
    death_sound = open("death_sound.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    back_music_time = 0

    # sets player to all of the player sprites
    #player = [player1] + [player2] + [player3] + [player4]

    knifes = []
    for knife_number in range(constants.TOTAL_NUMBER_OF_KNIFES):
        a_single_knife = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        knifes.append(a_single_knife)


    # displays the background and sets the frame rate to 60
    game = stage.Stage(ugame.display, 60)

    # sets the layers of the sprites
    game.layers = [score_text] + enemys + knifes + [player1] + [player2] + [player3] + [player4] + [background]

    # render all of the sprites
    game.render_block()

    while True:
        # handle inputs
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]
            pass
        if keys & ugame.K_O:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if (player3.x + 10) < 160:
                player1.move(player1.x + 1, player1.y)
                player2.move(player2.x + 1, player2.y)
                player3.move(player3.x + 1, player3.y)
                player4.move(player4.x + 1, player4.y)
            else:
                player1.move(134, player1.y)
                player2.move(134, player2.y)
                player3.move(150, player3.y)
                player4.move(150, player4.y)
        if keys & ugame.K_LEFT:
            if (player1.x + 6) > 0:
                player1.move(player1.x - 1, player1.y)
                player2.move(player2.x - 1, player2.y)
                player3.move(player3.x - 1, player3.y)
                player4.move(player4.x - 1, player4.y)
            else:
                player1.move(-6, player1.y)
                player2.move(-6, player2.y)
                player3.move(10, player3.y)
                player4.move(10, player4.y)

        if keys & ugame.K_UP:
            pass
            #player1.move(player1.x, player1.y - 1)
            #player2.move(player2.x, player2.y - 1)
            #player3.move(player3.x, player3.y - 1)
            #player4.move(player4.x, player4.y - 1)
        if keys & ugame.K_DOWN:
            pass
            #player1.move(player1.x, player1.y + 1)
            #player2.move(player2.x, player2.y + 1) 
            #player3.move(player3.x, player3.y + 1) 
            #player4.move(player4.x, player4.y + 1)         


        if a_button == constants.button_state["button_just_pressed"]:
            for knife_number in range(len(knifes)):
                if knifes[knife_number].x < 0:
                    knifes[knife_number].move(player1.x + 8, player1.y)
                    sound.play(pew_sound)
                    break


        for knife_number in range(len(knifes)):
            if knifes[knife_number].x > 0:
                knifes[knife_number].move(knifes[knife_number].x, knifes[knife_number].y - constants.KNIFE_SPEED)
                if knifes[knife_number].y < constants.OFF_TOP_SCREEN:
                    knifes[knife_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)    

        for knife_number in range(len(knifes)):
            if knifes[knife_number].x > 0:
                for enemy_number in range(len(enemys)):
                    if enemys[enemy_number].x > 0:
                        if stage.collide(knifes[knife_number].x + 6, knifes[knife_number].y + 2, knifes[knife_number].x + 11, knifes[knife_number].y + 12, enemys[enemy_number].x + 1, enemys[enemy_number].y, enemys[enemy_number].x + 15, enemys[enemy_number].y + 15):
                            enemys[enemy_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            knifes[knife_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(hit_sound)
                            show_enemy()
                            show_enemy()
                            score += 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text(f"Score: {score}")

        for enemy_number in range(len(enemys)):
            if enemys[enemy_number].x > 0:
                enemys[enemy_number].move(enemys[enemy_number].x, enemys[enemy_number].y + constants.ENEMY_SPEED)
                if enemys[enemy_number].y > constants.SCREEN_Y:
                    enemys[enemy_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)    
                    show_enemy()
                    score -= 1
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text(f"Score: {score}")

        for enemy_number in range(len(enemys)):
            if enemys[enemy_number].x > 0:
                if stage.collide(enemys[enemy_number].x + 6, enemys[enemy_number].y + 2, enemys[enemy_number].x + 11, enemys[enemy_number].y + 12, player1.x, player1.y, player1.x + 25, player1.y + 25):
                    sound.stop()
                    sound.play(death_sound)
                    time.sleep(3.0)
                    game_over_scene(score)
        
        # if back_music_time >= 838:
        #     sound.play(back_music)
        #     back_music_time = 0
        # else:
        #     back_music_time += 1


        # renders the sprite every frame
        game.render_sprites([player1] + [player2] + [player3] + [player4] + knifes + enemys)

        # only ticks every 1/60th of a second
        game.tick()

def game_over_scene(final_score):
    sound = ugame.audio
    sound.stop()

    image_bank_2 = stage.Bank.from_bmp16("pain_menu.bmp")

    background =  stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(24, 20)
    text1.text(f"Final Score: {final_score}")
    text.append(text1)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(43, 60)
    text3.text(f"GAME OVER")
    text.append(text3)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text(f"PRESS SELECT")
    text.append(text2)

    game = stage.Stage(ugame.display, constants.FPS)

    game.layers = text + [background]

    game.render_block()

    music = open("rick.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(music)

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

            game.tick()

if __name__ == "__main__":
    splash_screen()
