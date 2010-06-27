#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable-msg=W0312
import pygame.font,pygame.mixer
pygame.font.init()
pygame.mixer.init()
HUMAN=0
AI=1

# Options
RESX=800
RESY=600
PLAYER1=HUMAN
PLAYER2=AI
TOWER_VICTORY=100
RESSOURCE_VICTORY=int(TOWER_VICTORY*1.5)
INIT_VAL=int(RESSOURCE_VICTORY/10)
INIT_INC=int(INIT_VAL/10)

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
