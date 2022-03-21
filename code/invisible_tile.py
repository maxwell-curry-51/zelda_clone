import pygame 
from settings import *

class InvisibleTile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/png/transparent.png').convert_alpha()		
		# self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()

		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)
		self.remove = False
		self.name = 'not floor'
		
		self.health = 666
