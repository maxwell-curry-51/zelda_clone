import pygame 
from settings import *

class PolyBarrier(pygame.sprite.Sprite):
	def __init__(self,pos,groups,segments):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/png/test_wall.png').convert_alpha()
		WHITE=(255,255,255)
		if segments == (1,0,1,0):
			#left wall
			print('true')
			self.rect = self.image.get_rect(topleft = pos)
			# self.rect = pygame.Rect(WHITE, (0,0,32, 64))
			# self.hitbox = self.rect.inflate(0,0)
			self.hitbox = pygame.Rect(self.rect.topleft, (32, 64)) #self.rect.inflate(0,-10)
			self.remove = False
			self.name = 'not floor'
		else : 
			#implement debug mode for wall transparency
			self.rect = self.image.get_rect(topleft = pos)
			self.hitbox = self.rect.inflate(0,0)
			self.remove = False
			self.name = 'not floor'
		
		self.health = 666
		
		# self.hitbox = pygame.Rect(self.rect.midtop, (32, 64)) right
