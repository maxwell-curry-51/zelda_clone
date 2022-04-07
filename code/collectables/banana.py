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
		
		# self.health = float('inf')
		# # get sprite sheet
		# self.image = pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64))
		# self.rect = self.image.get_rect(topleft = pos)

		# # get specific sprite
		# self.spike_sprite_location_x = 7
		# self.spike_sprite_location_y = 1
		# self.sprite_location = ((64 * self.spike_sprite_location_x),(64 * self.spike_sprite_location_y),64,64)

		# # set hitbox
		# self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
		
		# self.health = float('inf')
		# self.name = 'spikes'
