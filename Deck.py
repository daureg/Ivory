#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable=W0312,W0612
"""Implementation of Deck object."""
import os, os.path, random, Card, Const
class Deck:
	"""Construct a list of cards while maintaining information over those which
are in game."""
	def __init__(self, exemplary = 5):
		"""Reads cards in CARDS_DIR and build them exemplary times."""
		available = (c for c in os.listdir(Const.CARDS_DIR) if c.endswith(".card"))
		self.cards = []
		for i in available:
			for j in xrange(1, exemplary):
				self.cards.append(Card.Card(os.path.join(Const.CARDS_DIR, i)))
		self.ingame = []
		self.rnd = random.Random()

	def get_card(self, pos):
		"""Give a random card and place it ingame and in 'pos'."""
		idx = self.rnd.randint(0, len(self.cards) - 1)
		card = self.cards[idx]
		self.cards.remove(card)
		self.ingame.append(card)
		card.set_pos(pos)
		return card

	def played_card(self, card):
		"""Return the pos of a played card."""
		self.ingame.remove(card)
		self.cards.append(card)
		return card.box_pos
