import pygame 
from settings import *

class FloorTile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#get spritesheet
		self.image_raw = pygame.image.load('../graphics/dungeon/tiles-eastern-palace.png').convert_alpha()
		self.image = pygame.transform.scale2x(pygame.transform.scale2x(self.image_raw))
		self.rect = self.image.get_rect(topleft = pos)

		#floortile specific vars
		self.hitbox = pygame.Rect(pos[0],pos[1],64,64)#)self.rect.inflate(-10,-10)
		self.remove = False
		self.sprite_location = (13,(486*2) + 1,64,64)
		self.name = 'floor'
		
		self.health = 666
