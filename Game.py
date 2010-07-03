#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable=W0312
"""Main Game class implementation"""
import pygame
import Const, Deck, Player

def evaluate(card, owner, ennemy):
	"""If 'owner' plays 'card' against 'ennemy', return true if
	card's condition is verified"""
	if card.condition == "":
		return True
	import re
	value = r"[OE][TWBQGMDC]"
	comp = r"(?:<|>|<=|>=|==|!=)"
	num = r"(?:\+|-)?[0-9]+"
	clause = r"\s*(%s)\s+(%s)\s+(%s|%s)" % (value, comp, num, value)
	match = re.match(clause, card.condition)
	left = match.groups()[0].lower()
	comp = match.groups()[1]
	right = match.groups()[2].lower()
	get_value = {"ot" : owner.get_t(), "ow" : owner.get_w(), \
		"ob" : owner.get_b(), "og" : owner.get_g(), "oc" : owner.get_c(), \
		"oq" : owner.get_q(), "om" : owner.get_m(), "od" : owner.get_d(), \
		"et" : ennemy.get_t(), "ew" : ennemy.get_w(), \
		"eb" : ennemy.get_b(), "eg" : ennemy.get_g(), "ec" : ennemy.get_c(), \
		"eq" : ennemy.get_q(), "em" : ennemy.get_m(), "ed" : ennemy.get_d()}
	a = int(get_value[left])
	if right[0] in ['o', 'e']:
		b = int(get_value[right])
	else:
		b = int(right)
	return {"<" : a < b, ">" : a > b, "<=" : a <= b, \
			">=" : a >= b, "==" : a == b, "!=" : a != b}[comp]

def apply_card(card, owner, ennemy):
	"""Make card's effects happens"""
	owner.change_b(-card.cost[0])
	owner.change_g(-card.cost[1])
	owner.change_c(-card.cost[2])
	chose_then = evaluate(card, owner, ennemy)
	if chose_then:
		leff = card.then_l
	else:
		leff = card.else_l
	function = [owner.change_t, owner.change_w, owner.change_b, owner.change_q, \
		owner.change_g, owner.change_m, owner.change_c, owner.change_d, \
		ennemy.change_t, ennemy.nothing, ennemy.change_b, ennemy.change_q, \
		ennemy.change_g, ennemy.change_m, ennemy.change_c, ennemy.change_d]
	for (func, value) in zip(function, leff):
		func(value)
	ennemy.change_t(ennemy.change_w(leff[10]))

class Game:
	"""Handle players, deck and main loop"""
	def __init__(self):
		"""Initialize all objects"""
		pygame.display.init()
		if Const.FULLSCREEN:
			flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
		else:
			flags = 0
		self.screen = pygame.display.set_mode((Const.RESX, Const.RESY), flags)
		pygame.display.set_caption("Ivory")
		self.running = True
		self.deck = Deck.Deck()
		self.player_1 = Player.Player(self.deck, True)
		self.player_2 = Player.Player(self.deck, False)
		self.turn = 1
		self.players = {1 : self.player_1, 2 : self.player_2}
		self.who = Const.INFO_FONT.render(_("It's Player %d's turn"%(self.turn)),
				True, Const.LEFT_COLOR)
		self.who_pos = (0.5*(Const.RESX - self.who.get_width()), Const.RESY/16)


	def __del__(self):
		"""Quit all pygame module"""
		pygame.mixer.quit()
		pygame.font.quit()
		pygame.display.quit()

	def run(self):
		"""Main loop"""
		font = Const.WINNER_FONT
		text_pos = (.5*(Const.RESX - font.size(_("Player 1 wins!"))[0]),
			.5*(Const.RESY - font.get_linesize()))
		while not self.player_1.win and not self.player_2.win and self.running:
			chosen = None
			for event in pygame.event.get():
				if event.type == pygame.QUIT or \
				event.type == pygame.KEYDOWN: self.running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					chosen, again, discard = self.players[self.turn].click(event)
			if chosen != None:
				self.play_card(self.players[self.turn], chosen, again, discard)
			self.screen.fill(Const.BLACK)
			self.player_1.draw(self.screen, self.turn == 1)
			self.player_2.draw(self.screen, self.turn == 2)
			self.screen.blit(self.who, self.who_pos)
			pygame.display.flip()

		if self.player_1.win:
			text = font.render(_("Player 1 wins!"), True, Const.LEFT_COLOR)
		else:
			text = font.render(_("Player 2 wins!"), True, Const.RIGHT_COLOR)

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or \
				event.type == pygame.KEYDOWN or \
				event.type == pygame.MOUSEBUTTONDOWN:
					self.running = False
			self.screen.fill(Const.BLACK)
			self.screen.blit(text, text_pos)
			pygame.display.flip()
	
	def play_card(self, player, chosen, again, discard):
		"""Change turn when a card have been played"""
		player.card_out(chosen)
		if self.turn == 1:
			new_turn = 2
		else:
			new_turn = 1
		if not discard:
			apply_card(chosen, player, self.players[new_turn])
		if not again:
			self.turn = new_turn
		self.player_1.end_turn(self.player_2)
		self.player_2.end_turn(self.player_1)

		who_font = Const.INFO_FONT
		colors = {1 : Const.LEFT_COLOR, 2 : Const.RIGHT_COLOR}
		self.who = who_font.render(_("It's Player %d's turn"%(self.turn)),
				True, colors[self.turn])
