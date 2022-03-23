import pygame 
from settings import *

class Barrier(pygame.sprite.Sprite):
	def __init__(self,pos,groups,debug):
		super().__init__(groups)
		#implement debug mode for wall transparency
		if debug:
			self.image = pygame.image.load('../graphics/png/test_wall.png').convert_alpha()
		else:
			self.image = pygame.image.load('../graphics/png/transparent.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,0)
		self.remove = False
		self.name = 'not floor'
		
		self.health = float('inf')
