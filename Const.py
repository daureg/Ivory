#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable-msg=W0312
import options

def clamp(x, s, e):
	return min(max(x,s),e)

def available_mode(s):
	if s.strip() in ["human", "ai"]:
		return s.strip()
	else:
		return "human"

import pygame.font,pygame.mixer,sys
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
PLAYER1=available_mode(options.PLAYER1)
PLAYER2=available_mode(options.PLAYER2)
TOWER_VICTORY=clamp(options.TOWER_VICTORY, 20, 500)
INIT_TOWER=clamp(options.INIT_TOWER, 2, 50)
RESSOURCE_VICTORY=clamp(options.RESSOURCE_VICTORY, 35, 750)
INIT_VAL=clamp(options.INIT_VAL, 3, 75)
INIT_INC=clamp(options.INIT_INC, 1, 7)
RESX=clamp(options.RESX, 100, 3000)
RESY=clamp(options.RESY, 100, 3000)
FULLSCREEN=bool(options.FULLSCREEN)

# Dimensions
CARD_HEIGHT=RESY/3
ROOF_HEIGHT=RESY/8
# Colors
BLACK=(0,0,0)
LIGHT_BLACK=(128,0,0)
GREY=(128,128,128)
ALPHA_GREY=(128,128,128,128)
WHITE=(255,255,255)
RED=(255,0,0)
LIGHT_RED=(128,0,0)
GREEN=(0,255,0)
LIGHT_GREEN=(0,128,0)
BLUE=(0,0,255)
LIGHT_BLUE=(0,0,128)
LEFT_COLOR=(255,0,0)
RIGHT_COLOR=(0,0,255)
# Fonts
FONT_FILE="DejaVuLGCSans.ttf"
BUILDING_FONT=pygame.font.Font(FONT_FILE, 20)
INC_FONT=pygame.font.Font(FONT_FILE, 20)
VAL_FONT=pygame.font.Font(FONT_FILE, 14)
CARD_FONT=pygame.font.Font(FONT_FILE, 10)
# Sounds
RES_POS_SOUND=pygame.mixer.Sound("tada.wav")
RES_NEG_SOUND=pygame.mixer.Sound("tada.wav")
BUILD_POS_SOUND=pygame.mixer.Sound("tada.wav")
BUILD_NEG_SOUND=pygame.mixer.Sound("tada.wav")
