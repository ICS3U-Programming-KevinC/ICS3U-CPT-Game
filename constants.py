# !/user/bin/env python3
 
# Created by Kevin Csiffary
# Date: Jan. 11, 2023
# This is the constants file for my game

SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ENEMYS = 5
TOTAL_NUMBER_OF_KNIFES = 5
PLAYER_SPEED = 1
ENEMY_SPEED = 1
KNIFE_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}

RED_PALETTE = ( b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff' 
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')