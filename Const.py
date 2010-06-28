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

import pygame.font,pygame.mixer
pygame.font.init()
pygame.mixer.init()

# Options
PLAYER1=available_mode(options.PLAYER1)
PLAYER2=available_mode(options.PLAYER2)
TOWER_VICTORY=clamp(options.TOWER_VICTORY, 20, 500)
INIT_TOWER=TOWER_VICTORY/10
RESSOURCE_VICTORY=int(clamp(options.RESSOURCE_VICTORY, 35, 750)
INIT_VAL=int(clamp(options.INIT_VAL, 3, 75))
INIT_INC=int(clamp(options.INIT_INC, 1, 7))
RESX=clamp(options.RESX, 100, 3000)
RESY=clamp(options.RESY, 100, 3000)
FULLSCREEN=bool(options.FULLSCREEN)

# Private
CARD_HEIGHT=int(RESY/3)
LEFT_COLOR=(255,0,0)
RIGHT_COLOR=(0,0,255)
BUILDING_FONT=pygame.font.SysFont("gentium", 20, True)
INC_FONT=pygame.font.SysFont("gentium", 20, True)
VAL_FONT=pygame.font.SysFont("gentium", 14, True)
ROOF_HEIGHT=int(RESY/8)
RES_POS_SOUND=pygame.mixer.Sound("tada.wav")
RES_NEG_SOUND=pygame.mixer.Sound("tada.wav")
