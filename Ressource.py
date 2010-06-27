#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable-msg=W0312
import Const, pygame
class Ressource:
	def __init__(self, pos, color, text, image=""):
		self.box_pos = pos
		self.w = int(Const.RESX/8)
		self.h = int(Const.RESY/7)
		x=self.box_pos[0]
		y=self.box_pos[1]
		w=self.w
		h=self.h
		self.color = color
		self.desc = text
		#self.pic = pygame.image.load(image)
		#self.pic_pos = (x,y)
		self.pos_sound = Const.RES_POS_SOUND
		self.neg_sound = Const.RES_NEG_SOUND
		self.inc = Const.INIT_INC
		self.val = Const.INIT_VAL
		self.inc_font = Const.INC_FONT
		self.inc_text = self.inc_font.render("%d"%self.inc, True, (255,255,255))
		self.inc_text_pos = (int(x+w/10),int(y+h/10))
		self.val_font = Const.VAL_FONT
		self.val_text = self.val_font.render("%d %s"%(self.val,self.desc), True, (255,255,255))
		self.val_text_pos = (int(x+w/15),int(y+7*h/10))
		self.box = pygame.Surface((w,h))
		self.box.fill(self.color)
	
	def draw(self, screen):
		screen.blit(self.box,self.box_pos)
		screen.blit(self.inc_text,self.inc_text_pos)
		screen.blit(self.val_text,self.val_text_pos)
		#screen.blit(self.pic,self.pic_pos)

	def change_inc(self, value):
		self.inc = max(1, self.inc + value)
		self.inc_text = self.inc_font.render("%d"%self.inc, True, (255,255,255))
		if value>0:
			self.pos_sound.play()
		if value<0:
			self.neg_sound.play()
	
	def change_val(self, value):
		self.val = min(max(0, self.val + value), Const.RESSOURCE_VICTORY)
		self.val_text = self.val_font.render("%d %s"%(self.val,self.desc), True, (255,255,255))
		if value>0:
			self.pos_sound.play()
		if value<0:
			self.neg_sound.play()
	
	def val(self):
		return self.val
	
	def inc(self):
		return self.inc
	
