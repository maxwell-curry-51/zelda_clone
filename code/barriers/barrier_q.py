import pygame 
from settings import *

class BarrierQ(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#implement debug mode for wall transparency
		self.image = pygame.image.load('../graphics/png/test_wall_q.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,0)
		self.remove = False
		self.name = 'not floor'
		
		self.health = 666
