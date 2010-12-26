#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable=W0312
"""Various global constants."""
from __future__ import print_function
import os, os.path
import options
def clamp(val, start, end):
	"""Clamp val between start and end."""
	return min(max(val, start), end)

def available_mode(mode):
	"""mode can only be 'ai' or 'human' (default)."""
	if mode.strip() in ["human", "ai"]:
		return mode.strip()
	else:
		return "human"

import pygame.font, pygame.mixer, sys
if pygame.font:
	pygame.font.init()
else:
	print(_("You need SDL_tff!"))
	sys.exit()
if pygame.mixer:
	pygame.mixer.init()
else:
	print(_("You need SDL_mixer!"))
	sys.exit()

# Options
PLAYER1 = available_mode(options.PLAYER1)
PLAYER2 = available_mode(options.PLAYER2)
TOWER_VICTORY = clamp(options.TOWER_VICTORY, 20, 500)
INIT_TOWER = clamp(options.INIT_TOWER, 2, 50)
RESSOURCE_VICTORY = clamp(options.RESSOURCE_VICTORY, 35, 750)
INIT_VAL = clamp(options.INIT_VAL, 3, 75)
INIT_INC = clamp(options.INIT_INC, 1, 7)
RESX = clamp(options.RESX, 100, 3000)
RESY = clamp(options.RESY, 100, 3000)
FULLSCREEN = bool(options.FULLSCREEN)

# Dimensions
CARD_HEIGHT = RESY/3
ROOF_HEIGHT = RESY/8
# Dir
DATA_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))
CARDS_DIR = os.path.join(DATA_DIR, 'cards')
LOCALE_DIR = os.path.join(DATA_DIR, 'locale')
# Colors
BLACK = (0, 0, 0)
LIGHT_BLACK = (128, 0, 0)
GREY = (128, 128, 128)
ALPHA_GREY = (128, 128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (128, 0, 0)
DARK_RED = (192, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 128, 0)
DARK_GREEN = (0, 192, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 0, 128)
DARK_BLUE = (0, 0, 192)
LEFT_COLOR = (255, 0, 0)
RIGHT_COLOR = (0, 0, 255)
# Fonts
FONT_FILE = os.path.join(DATA_DIR, "DejaVuLGCSans.ttf")
BUILDING_FONT = pygame.font.Font(FONT_FILE, 20)
INC_FONT = BUILDING_FONT
VAL_FONT = pygame.font.Font(FONT_FILE, 14)
INFO_FONT = INC_FONT
CARD_FONT = pygame.font.Font(FONT_FILE, 10)
WINNER_FONT = pygame.font.Font(FONT_FILE, 36)
# Sounds
RES_POS_SOUND = pygame.mixer.Sound("tada.wav")
RES_NEG_SOUND = pygame.mixer.Sound("tada.wav")
BUILD_POS_SOUND = pygame.mixer.Sound("tada.wav")
BUILD_NEG_SOUND = pygame.mixer.Sound("tada.wav")
