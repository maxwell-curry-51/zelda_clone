import pygame 
from settings import *

class Portal(pygame.sprite.Sprite):
	def __init__(self,pos,groups, tag):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/png/transparent.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(64,-32)
		self.remove = False
		self.next_map = tag[0]
		self.spawn_point = tag[1]
		self.spawn_centering = tag[2]
		self.name = 'not floor'

		
		self.health = 666
