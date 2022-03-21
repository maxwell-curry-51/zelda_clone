import pygame 
from settings import *

class BarrierR(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#implement debug mode for wall transparency
		self.image = pygame.image.load('../graphics/png/test_wall_v.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = pygame.Rect(self.rect.topright, (32, 64)) #self.rect.inflate(0,-10)
		self.remove = False
		self.name = 'right'
		
		self.health = 666