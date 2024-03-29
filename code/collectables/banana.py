import pygame 
from settings import *
from spritesheet import SpriteSheet


class Banana(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		
		# used for state management
		self.pos = pos
		
		self.image_raw = pygame.image.load('../graphics/collectables/banana.png').convert_alpha()
		self.image = pygame.transform.scale(self.image_raw, (50, 50))
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,0)
		self.remove = False
		self.name = 'banana'
