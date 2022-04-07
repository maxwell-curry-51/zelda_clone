import pygame 
from settings import *
from spritesheet import SpriteSheet


class Merchant(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)

		self.image = pygame.transform.scale(pygame.image.load('../graphics/player_sprites/merchant.png'),(256, 256)).convert_alpha()

		# get sprite sheet
		# self.image = pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64))
		self.rect = self.image.get_rect(topleft = pos)

		# get specific sprite
		# self.spike_sprite_location_x = 2
		# self.spike_sprite_location_y = 7
		# self.sprite_location = ((64 * self.spike_sprite_location_x),(64 * self.spike_sprite_location_y),64,64)

		# set hitbox
		self.hitbox = self.rect
		
		# conversation bubble
		self.talking_points = [['message 1a', 'message 1b', 'message 1c'],['message 2a', 'message 2b', 'message 2c'],['message 3a', 'message 3b', 'message 3c'],]
		self.talking_point_iterator = 0

		self.health = float('inf')
		self.name = 'merchant'

		
		self.chat_offset = pygame.math.Vector2()
		self.chat_offset.x = 64
		self.chat_offset.y = -64

	def talk(self, talking_string):
		print(talking_string)
