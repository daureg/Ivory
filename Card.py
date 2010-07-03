#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable=W0312
"""Card implementation."""
import Const, pygame, ConfigParser
DEFAULT = {'image' : 'void.png', 'description' : '', \
	 'play_again' : 'false', 'discard' : 'false', \
	 'b' : '0', 'g' : '0', 'c'  :'0', 'if' : '', \
	 'ot' : '0', 'ow' : '0', 'ob' : '0', 'oq' : '0', \
	 'og' : '0', 'om' : '0', 'oc' : '0', 'od' : '0', \
	 'et' : '0', 'ew' : '0', 'eb' : '0', 'eq' : '0', \
	 'eg' : '0', 'em' : '0', 'ec' : '0', 'ed' : '0' }

def inc_tupple(tup, fst, snd):
	"Add a tupple with (fst, snd)."""
	return (tup[0]+fst, tup[1]+snd)

def text_format(text, width, start, font, decal=0):
	"""Return line of text and their position no longer than 'width'."""
	import re
	init_x = start[0] + decal
	init_y = start[1]
	i = 0
	lsize = 3*font.get_linesize()/2
	results = []
	results_pos = []
	todo = re.sub(r'\s+', r' ', text.strip()).split()
	while todo != []:
		i = 1
		while i < len(todo) and font.size(' '.join(todo[0:i]))[0] < (width-decal):
			i += 1
		results.append(' '.join(todo[0:i-1]))
		results_pos.append((init_x, init_y+len(results)*lsize))
		todo = todo[i-1:]
		if len(todo) == 1:
			results.append(todo[0])
			results_pos.append((init_x, init_y+len(results)*lsize))
			todo = []
	return (results, results_pos)

def read_cost(parser):
	"""Read cost and return it with appropriate color"""
	brick = parser.getint('Cost', 'b')
	gem = parser.getint('Cost', 'g')
	crea = parser.getint('Cost', 'c')
	if max(brick, gem, crea) == brick:
		color = Const.LIGHT_RED
	if max(brick, gem, crea) == gem:
		color = Const.LIGHT_BLUE
	if max(brick, gem, crea) == crea:
		color = Const.LIGHT_GREEN
	return (brick, gem, crea), color

class Card:
	"""A graphic card with a list of effects and other informations."""
	def __init__(self, filename, pos=(0, 0)):
		"""Parse 'filename' to build a card."""
		parser = ConfigParser.SafeConfigParser(DEFAULT)
		parser.read(filename)
		self.then_l = []
		self.else_l = []
		self.name = parser.get('General', 'name')
		self.img = parser.get('General', 'image')
		self.desc = parser.get('General', 'description')
		self.again = parser.getboolean('General','play_again')
		self.discard = parser.getboolean('General','discard')
		self.cost, self.color = read_cost(parser)
		self.condition = parser.get('Condition', 'if')
		self.read_effect(parser, "then")
		self.read_effect(parser, "else")
		# TODO self.value, self.type
		x = pos[0]
		y = pos[1]
		w = Const.RESX/7
		h = Const.CARD_HEIGHT
		self.w = w
		self.h = h
		self.box = pygame.Surface((w, h))
		self.box_pos = (x, y)
		self.box.fill(self.color)
		self.expensive = pygame.Surface((w+4, h+4))
		self.expensive_pos = (x-2, y-2)
		self.expensive.fill(Const.GREY)
		self.expensive.set_alpha(128)
		self.name_text = Const.CARD_FONT.render("%s"%self.name, True, Const.WHITE)
		self.name_pos = (x+h/10, y+w/10)
		#self.pic = load
		#self.pic_pos = 
		text, self.desc_pos = text_format(self.get_desc(),
				w, (x, y+2*h/10), Const.CARD_FONT, w/40)
		self.desc_text = map(lambda x: Const.CARD_FONT.render(x, True, Const.WHITE),
				text)
		if self.cost[0] == 0:
			self.cost_b = Const.CARD_FONT.render(" %.2d "%self.cost[0],
					True, self.color)
		else:                                             
			self.cost_b = Const.CARD_FONT.render(" %.2d "%self.cost[0], 
					True, Const.WHITE, Const.RED)
		self.cost_b_pos = (x+w/10, y+9*h/10)              
                                                                  
		if self.cost[1] == 0:                             
			self.cost_g = Const.CARD_FONT.render(" %.2d "%self.cost[1], 
					True, self.color)
		else:                                             
			self.cost_g = Const.CARD_FONT.render(" %.2d "%self.cost[1], 
					True, Const.WHITE, Const.BLUE)
		self.cost_g_pos = (x+4*w/10, y+9*h/10)            
                                                                  
		if self.cost[2] == 0:                             
			self.cost_c = Const.CARD_FONT.render(" %.2d "%self.cost[2], 
					True, self.color)
		else:                                             
			self.cost_c = Const.CARD_FONT.render(" %.2d "%self.cost[2], 
					True, Const.BLACK, Const.GREEN)
		self.cost_c_pos = (x+8*w/10, y+9*h/10)
	



	def read_effect(self, parser, effect):
		"""Fill 'effect' list."""
		var = ["ot", "ow", "ob", "oq", "og", "om", "oc", "od", \
			"et", "ew", "eb", "eq", "eg", "em", "ec", "ed"]
		for i in var:
			if effect == "then":
				self.then_l.append(parser.getint('Then_Effect', i))
			else:
				self.else_l.append(parser.getint('Else_Effect', i))

		
			
		
	def get_desc(self):
		"""Build a decription of the card according to its effects."""
		desc = ""
		trans = [_("OT"), _("OW"), _("OB"), _("OQ"), \
			 _("OG"), _("OM"), _("OC"), _("OD"), \
			 _("ET"), _("EW"), _("EB"), _("EQ"), \
			 _("EG"), _("EM"), _("EC"), _("ED")]
		if self.condition != "":
			desc += _("if ") + self.condition + _(" then ")
		for i, value in enumerate(self.then_l):
			if value != 0:
				desc += trans[i] + ":" + str(value) + " "
		if self.condition != "":
			desc += _("else ")
		for i, value in enumerate(self.else_l):
			if value != 0:
				desc += trans[i] + ":" + str(value) + " "
		if self.again:
			desc += _("play again ")
		if self.discard:
			desc += _("discard one card ")
		return desc

	def draw(self, screen, mode):
		"""Draw the card with respect to 'mode' -> "hidden" or "ai"."""
		screen.blit(self.box, self.box_pos)
		screen.blit(self.name_text, self.name_pos)
		for (text, pos) in zip(self.desc_text, self.desc_pos):
			screen.blit(text, pos)
		screen.blit(self.cost_b, self.cost_b_pos)
		screen.blit(self.cost_g, self.cost_g_pos)
		screen.blit(self.cost_c, self.cost_c_pos)
		if mode == "hidden":
			screen.blit(self.expensive, self.expensive_pos)

	def set_pos(self, pos):
		"""Change the position of the card."""
		diff_x = pos[0] - self.box_pos[0]
		diff_y = pos[1] - self.box_pos[1]
		self.box_pos = inc_tupple(self.box_pos, diff_x, diff_y)
		self.expensive_pos = inc_tupple(self.expensive_pos, diff_x, diff_y)
		self.name_pos = inc_tupple(self.name_pos, diff_x, diff_y)
		for i in xrange(0, len(self.desc_pos)):
			self.desc_pos[i] = inc_tupple(self.desc_pos[i], diff_x, diff_y)
		self.cost_b_pos = inc_tupple(self.cost_b_pos, diff_x, diff_y)
		self.cost_g_pos = inc_tupple(self.cost_g_pos, diff_x, diff_y)
		self.cost_c_pos = inc_tupple(self.cost_c_pos, diff_x, diff_y)
