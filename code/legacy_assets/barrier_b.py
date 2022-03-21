import pygame 
from settings import *

class BarrierB(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#implement debug mode for wall transparency
		self.image = pygame.image.load('../graphics/png/test_wall_h.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = pygame.Rect(self.rect.bottomleft, (64, 32)) #self.rect.inflate(0,-10)
		self.remove = False
		self.name = 'bottom'
		
		self.health = 666