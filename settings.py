import pygame as pg


# Initialize Sound
pg.mixer.init()


# Audio files
pad_hit = pg.mixer.Sound('audio/pad_hit.ogg')
brick_breaking = pg.mixer.Sound("audio/brick_breaking.ogg")
game_end = pg.mixer.Sound("audio/game_end_.ogg")
dropping_ball = pg.mixer.Sound("audio/dropping_ball.ogg")
win_game = pg.mixer.Sound("audio/win_game.ogg")


# Screen dimensions
WIDTH = 550
HEIGHT = 600

BG_COLOR = "purple"

# Text color
color = "white"


# Paddle settings
paddle_x = 200
paddle_y = 550
paddle_width = 100
paddle_height = 20


# Ball settings
ball_x = 250
ball_y = 540
ball_x_speed = 2
ball_y_speed = 2
ball_radius = 5


# Text settings
text_x = 300


# Bricks settings
brick_width = 40
brick_height = 20