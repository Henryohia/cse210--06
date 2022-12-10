import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Demolisher"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH
COLUMNS_WIDTH = 80
ROW_HEIGHT = 28

# FONT
FONT_FILE = "demolisher/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "demolisher/assets/sounds/boing.wav"
WELCOME_SOUND = "demolisher/assets/sounds/start.wav"
OVER_SOUND = "demolisher/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4
VICTORY = 5

# LEVELS
LEVEL_FILE = "demolisher/assets/data/level-{:03}.txt"
BASE_LEVELS = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGES = [f"demolisher/assets/images/{i:03}.png" for i in range(0, 5)]
BALL_WIDTH = 54
BALL_HEIGHT = 54
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGE = "demolisher/assets/images/100.png"
RACKET_WIDTH = 45
RACKET_HEIGHT = 10
RACKET_VELOCITY = 10

#Bullets
BULLET_GROUP = "bullets"
BULLET_IMAGES = [f"demolisher/assets/images/{i:03}.png" for i in range(200, 202)]
BULLET_WIDTH = 14
BULLET_HEIGHT = 28
PLAYER_BULLET_VELOCITY = -6
ALIEN_BULLET_VELOCITY = 4

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "s": "demolisher/assets/images/010.png",
    "m": "demolisher/assets/images/020.png",
    "l": "demolisher/assets/images/030.png",
    "x": "demolisher/assets/images/040.png",
    "e": "demolisher/assets/images/050.png",
    "a": "demolisher/assets/images/060.png"
}
BRICK_WIDTH = 30
BRICK_HEIGHT = 30
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
WAS_Victory = "CONGLATURATIONS!"