import pygame 
from settings import *

class TileSM(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/png/transparent_sm.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)
		self.remove = False
		self.name = 'not floor'
		
		self.health = 666
