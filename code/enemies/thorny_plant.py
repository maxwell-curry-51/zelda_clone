import pygame 
from settings import *
from spritesheet import SpriteSheet


class ThornyPlant(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)

		# used for state management
		self.pos = pos

		# get sprite sheet
		self.image = pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64))
		self.rect = self.image.get_rect(topleft = pos)

		# get specific sprite
		self.spike_sprite_location_x = 6
		self.spike_sprite_location_y = 0
		self.sprite_location = ((64 * self.spike_sprite_location_x),(64 * self.spike_sprite_location_y),64,64)

		# set hitbox
		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
		
		self.health = 1
		self.attacked = False
		self.name = 'thorny_plant'

	def update(self):
		if self.health <= 0:
			self.kill()
