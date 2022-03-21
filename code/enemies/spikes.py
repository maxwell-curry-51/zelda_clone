import pygame 
from settings import *
from spritesheet import SpriteSheet


class Spikes(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)

		# get sprite sheet
		self.image = pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64))
		self.rect = self.image.get_rect(topleft = pos)

		# get specific sprite
		self.spike_sprite_location_x = 7
		self.spike_sprite_location_y = 1
		self.sprite_location = ((64 * self.spike_sprite_location_x),(64 * self.spike_sprite_location_y),64,64)

		# set hitbox
		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
		
		self.health = 666
		self.name = 'spikes'
