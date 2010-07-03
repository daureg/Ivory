#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable=W0312
"""Implementation of Building class"""
import pygame, Const
class Building:
	"""Represent a tower or a wall"""
	def __init__(self, left=True, tower=True, hp=10):
		"""By default, build a 'tower' on the 'left'"""
		x = Const.RESX
		y = Const.RESY
		self.coeff = (y-Const.CARD_HEIGHT-Const.ROOF_HEIGHT)/Const.TOWER_VICTORY
		self.hp = hp
		self.left = left
		self.tower = tower
		self.pos_sound = Const.BUILD_POS_SOUND
		self.neg_sound = Const.BUILD_NEG_SOUND
		self.font = Const.BUILDING_FONT
		self.text = self.font.render("%d"%self.hp, True, Const.WHITE)
		self.height = self.coeff*self.hp
		if tower:
			self.width = x/8
		else:
			self.width = x/16
		self.init_y = y-Const.CARD_HEIGHT-self.text.get_height()
		initial_y = self.init_y - self.height
		if (left and tower):
			self.pos = (3*x/16, initial_y)
		if (left and not tower):
			self.pos = (5*x/16 + x/20, initial_y)
		if (not left and tower):
			self.pos = (11*x/16, initial_y)
		if (not left and not tower):
			self.pos = (11*x/16 - x/20 - self.width, initial_y)
		self.text_pos = (self.pos[0]+(self.width-self.text.get_width())/2,
				self.init_y)
		if left:
			self.color = Const.LEFT_COLOR
		else:
			self.color = Const.RIGHT_COLOR
		self.body = pygame.Surface((self.width, self.height))
		self.body.fill(Const.GREY)
		
	def draw(self, screen):
		"""Draw the building"""
		screen.blit(self.text, self.text_pos)
		screen.blit(self.body, self.pos)
		w = self.width
		x = self.pos[0]
		y = self.pos[1]
		if self.tower:
			pygame.draw.polygon(screen, self.color , 
				[(x-w/6, y), (x+7*w/6, y), (x+w/2, y-Const.ROOF_HEIGHT)])

	def change(self, value):
		"""Change health point and return supplementary damage if the wall
		is destroyed"""
		self.hp = min(Const.TOWER_VICTORY, max(0, self.hp+value))
		self.build()
		if value > 0:
			self.pos_sound.play()
		if value < 0:
			self.neg_sound.play()
	
	def build(self):
		"""Build all the graphic elements"""
		self.height = self.coeff*self.hp
		self.pos = (self.pos[0], self.init_y - self.height)
		self.body = pygame.Surface((self.width, self.height))
		self.body.fill(Const.GREY)
		self.text = self.font.render("%d"%self.hp, True, Const.WHITE)
