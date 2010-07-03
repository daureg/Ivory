#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable=W0312
"""Implementation of Player class"""
import Const, Building, Ressource
class Player:
	"""Handle a tower, a wall and three ressources."""
	def __init__(self, deck, left=True):
		"""Build everything and get 6 cards from 'deck'"""
		res_x = Const.RESX
		res_y = Const.RESY
		pos_x = res_x-11*res_x/80
		if left:
			pos_x = res_x/80
		self.tower = Building.Building(left, True, Const.INIT_TOWER)
		self.wall = Building.Building(left, False, Const.INIT_TOWER/2)
		self.brick = Ressource.Ressource((pos_x, res_y/20),
				Const.DARK_RED, _("Bricks"))
		self.gem = Ressource.Ressource((pos_x, res_y/10+res_y/7),
				Const.DARK_BLUE, _("Gems"))
		self.crea = Ressource.Ressource((pos_x, 3*res_y/20+2*res_y/7),
				Const.DARK_GREEN, _("Creatures"))
		self.cards = []
		for i in xrange(1, 7):
			self.cards.append(deck.get_card())
			self.cards[-1:][0].set_pos((i*res_x/49+(i-1)*res_x/7,
				res_y-Const.CARD_HEIGHT))
		self.win = False
	
	def draw(self, screen, active):
		"""Draw all element while checking for not playable card."""
		self.tower.draw(screen)
		self.wall.draw(screen)
		self.brick.draw(screen)
		self.gem.draw(screen)
		self.crea.draw(screen)
		if active:
			for card in self.cards:
				if self.get_b() >= card.cost[0] and \
				   self.get_g() >= card.cost[1] and \
				   self.get_c() >= card.cost[2]:
					card.draw(screen, "ok")
				else:
					card.draw(screen, "hidden")

	def end_turn(self, ennemy):
		"""Check for victory and increments ressources"""
		if self.get_t() >= Const.TOWER_VICTORY or \
		self.get_b() >= Const.RESSOURCE_VICTORY or \
		self.get_g() >= Const.RESSOURCE_VICTORY or \
		self.get_c() >= Const.RESSOURCE_VICTORY or \
		ennemy.get_t() <= 0:
			self.win = True
		self.change_b(self.get_q())
		self.change_g(self.get_m())
		self.change_c(self.get_d())

	def get_t(self):
		return self.tower.hp
	def get_w(self):
		return self.wall.hp
	def get_b(self):
		return self.brick.val
	def get_q(self):
		return self.brick.inc
	def get_g(self):
		return self.gem.val
	def get_m(self):
		return self.gem.inc
	def get_c(self):
		return self.crea.val
	def get_d(self):
		return self.crea.inc
	def change_t(self, val):
		self.tower.change(val)
	def change_w(self, val):
		self.wall.change(val)
	def change_b(self, val):
		self.brick.change_val(val)
	def change_q(self, val):
		self.brick.change_inc(val)
	def change_g(self, val):
		self.gem.change_val(val)
	def change_m(self, val):
		self.gem.change_inc(val)
	def change_c(self, val):
		self.crea.change_val(val)
	def change_d(self, val):
		self.crea.change_inc(val)
