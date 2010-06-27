#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable-msg=W0312
import pygame,Const
class Building:
	def __init__(self,left=True,tower=True,hp=10):
		self.coeff=int((Const.RESY-Const.CARD_HEIGHT-Const.ROOF_HEIGHT)/Const.TOWER_VICTORY)
		self.hp = hp
		self.left = left
		self.tower = tower
		self.font = Const.BUILDING_FONT
		self.text = self.font.render("%d"%self.hp, True, (255,255,255))
		self.height = self.coeff*self.hp
		if tower:
			self.width = int(Const.RESX/8)
		else:
			self.width = int(Const.RESX/16)
		self.init_y = Const.RESY-Const.CARD_HEIGHT-self.text.get_height()
		initial_y = self.init_y - self.height
		if (left and tower):
			self.pos = (int(3*Const.RESX/16),initial_y)
		if (left and not tower):
			self.pos = (int(5*Const.RESX/16) + int(Const.RESX/20), initial_y)
		if (not left and tower):
			self.pos = (int(11*Const.RESX/16), initial_y)
		if (not left and not tower):
			self.pos = (int(11*Const.RESX/16) - int(Const.RESX/20) - self.width, initial_y)
		self.text_pos = (self.pos[0]+int((self.width-self.text.get_width())/2),self.init_y)
		if left:
			self.color = Const.LEFT_COLOR
		else:
			self.color = Const.RIGHT_COLOR
		self.body = pygame.Surface((self.width,self.height))
		self.body.fill((128,128,128))
		
	def draw(self,screen):
		screen.blit(self.text,self.text_pos)
		screen.blit(self.body,self.pos)
		w = self.width
		x = self.pos[0]
		y = self.pos[1]
		if self.tower:
			pygame.draw.polygon(screen, self.color , 
				[(int(x-w/6),y), (int(x+7*w/6),y), (int(x+w/2),y-Const.ROOF_HEIGHT)])

	def change(self,value):
		self.hp = min(Const.TOWER_VICTORY,max(0,self.hp+value))
		self.build()
	
	def build(self):
		self.height = self.coeff*self.hp
		self.pos = (self.pos[0],self.init_y - self.height)
		self.body = pygame.Surface((self.width,self.height))
		self.body.fill((128,128,128))
		self.text = self.font.render("%d"%self.hp, True, (255,255,255))

	



