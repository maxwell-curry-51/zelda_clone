import pygame
from enemies.enemy_fixed_paths import GENERIC_PATH 
from enemies.enemy_sprite_locations import * 
from enemies.enemy_move import * 
from collision import * 
from settings import *
from spritesheet import SpriteSheet


class TrackingEnemy(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites,player_sprite):
		#boundary box for movement
		super().__init__(groups)
		
		# get passed variables
		self.pos = pos
		self.obstacle_sprites = obstacle_sprites
		self.player_sprite = player_sprite
		self.name = 'tracking_enemy'

		#enemy sprite related setup (visual)
		self.image = IMAGE 
		self.rect = self.image.get_rect(topleft = self.pos)
		self.sprite_locations = SPRITE_LOCATIONS
		self.sprite_location = self.sprite_locations[1][0]
		#used for shifting attack sprites that are a different dimension than walking sprite
		self.dynamic_offset = pygame.math.Vector2(0,0)
		#enemy sprite related setup (hitbox)
		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64).inflate(0,0)

		# enemy movement setup
		self.movement_counter = 0
		self.direction = pygame.math.Vector2()
		self.last_direction = 0
		self.speed = 4
		
		#sprite health
		self.attacked = False
		self.attacked_incrementor = 0
		self.stunned = False
		self.stunned_incrementor = 0
		self.attack_direction = 0
		self.health = 5

	def input(self):
		#get player location
		
		if self.stunned:
			if self.stunned_incrementor < 20 + 20:
				self.stunned_incrementor = self.stunned_incrementor + 1
			else:
				self.stunned = False
				self.stunned_incrementor = 0
			
			self.direction.x = 0
			self.direction.y = 0
		else:
			#direct enemy movement
			for sprite in self.player_sprite:
				self.direction.x = sprite.hitbox.center[0] - self.hitbox.center[0]		
				self.direction.y = sprite.hitbox.center[1] - self.hitbox.center[1]
				self.direction = self.direction.normalize()
			if abs(self.direction.y) > abs(self.direction.x) and self.direction.y > 0:
				#down
				self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[3])
				self.image = IMAGE
				self.sprite_location =self.sprite_locations[3][self.movement_counter]
				self.last_direction = 3
			elif abs(self.direction.y) > abs(self.direction.x) and self.direction.y < 0:
				#up
				self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[2])
				self.image = IMAGE
				self.sprite_location =self.sprite_locations[2][self.movement_counter]
				self.last_direction = 2
			elif abs(self.direction.y) < abs(self.direction.x) and self.direction.x > 0:
				#right
				self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[0])

				#finally we will update the image that will be displayed
				self.image = IMAGE
				self.sprite_location =self.sprite_locations[0][self.movement_counter]
				self.last_direction = 0
			elif abs(self.direction.y) < abs(self.direction.x) and self.direction.x < 0:
				#left
				self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[1])

				#finally we will update the image that will be displayed
				self.image = pygame.transform.flip(IMAGE,True,False)
				self.sprite_location = self.sprite_locations[1][self.movement_counter]
			else:
				self.direction.x = 0
				self.direction.y = 0

	def update(self):		
		if self.health <= 0:
			self.kill()

		self.input()
		move(self)
