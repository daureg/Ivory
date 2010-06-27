#! /usr/bin/env python
# vim: set fileencoding=utf-8 :
# pylint: disable-msg=W0312
import gettext,sys,pygame
import Const,Building,Ressource
class Game:
	def __init__(self):
		gettext.install('ivory')
		pygame.display.init()
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
		self.screen = pygame.display.set_mode((Const.RESX,Const.RESY))
		pygame.display.set_caption("Ivory")
		self.running = True
		self.t1 = Building.Building(True,True)
		self.t2 = Building.Building(False,True)
		self.w1 = Building.Building(True,False)
		self.w2 = Building.Building(False,False)
		self.b1 = Ressource.Ressource((int(Const.RESX/80),
			int(Const.RESY/20)), (192,0,0), _("Bricks"))
		self.g1 = Ressource.Ressource((int(Const.RESX/80),
			int(2*Const.RESY/20)+Const.RESY/7), (0,0,192), _("Gems"))
		self.c1 = Ressource.Ressource((int(Const.RESX/80),
			int(3*Const.RESY/20)+2*Const.RESY/7), (0,192,0), _("Creatures"))
		self.b1 = Ressource.Ressource((int(Const.RESX/80),int(Const.RESY/20)), (192,0,0), _("Bricks"))
		self.b2 = Ressource.Ressource((int(Const.RESX-11*Const.RESX/80),
			int(Const.RESY/20)), (192,0,0), _("Bricks"))
		self.g2 = Ressource.Ressource((int(Const.RESX-11*Const.RESX/80),
			int(2*Const.RESY/20)+Const.RESY/7), (0,0,192), _("Gems"))
		self.c2 = Ressource.Ressource((int(Const.RESX-11*Const.RESX/80),
			int(3*Const.RESY/20)+2*Const.RESY/7), (0,192,0), _("Creatures"))

	def __del__(self):
		pygame.mixer.quit()
		pygame.font.quit()
		pygame.display.quit()

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or \
				event.type == pygame.KEYDOWN: self.running=False
				if event.type == pygame.USEREVENT+1:
					exp.play()	
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button==1:
						self.t1.change(5)
						self.c1.change_val(20)
					else:
						self.t1.change(-5)

			self.screen.fill((0,0,0))
			self.t1.draw(self.screen)
			self.t2.draw(self.screen)
			self.w1.draw(self.screen)
			self.w2.draw(self.screen)
			self.b1.draw(self.screen)
			self.g1.draw(self.screen)
			self.c1.draw(self.screen)
			self.b2.draw(self.screen)
			self.g2.draw(self.screen)
			self.c2.draw(self.screen)
			pygame.display.flip()

