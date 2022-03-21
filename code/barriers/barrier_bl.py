import pygame 
from settings import *

class BarrierBL(pygame.sprite.Sprite):
	def __init__(self,pos,groups,debug):
		super().__init__(groups)
		#implement debug mode for wall transparency
		if debug:
			self.image = pygame.image.load('../graphics/png/test_wall_q.png').convert_alpha()
		else:
			self.image = pygame.image.load('../graphics/png/transparent_sm.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = pygame.Rect(self.rect.bottomleft, (32, 32)).inflate(0,0)
		# self.hitbox.inflate(0,0)
		self.remove = False
		self.name = 'bottom_left'
		
		self.health = 666
