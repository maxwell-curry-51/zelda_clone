import pygame 
from pygame.locals import *
from settings import *
from spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites,player_sprite,portals,parent):
		super().__init__(groups)
		super().__init__(player_sprite)
		#add to list of things to draw
		super().__init__(obstacle_sprites)
		self.remove = False
		# filename = '../graphics/test/link_sheet.png'
		# piece_ss = SpriteSheet(filename)

		#pause functionality
		self.paused = False
		self.last_pause = pygame.time.get_ticks()

		#player movement animation
		self.images = []
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64)))
		self.sprite_locations = [[],[],[],[]]
		self.max_row = 8
		self.max_col = 10
		self.movement_counter = 0

		#fix me controlling animation changes by using copied list objects
		
		self.spritesheet_mapping = SAMPLE_1
		for row_index,row in enumerate(self.spritesheet_mapping):
			for col_index, col in enumerate(row):
				if col == 'pr':
					for i in range(6):
						self.sprite_locations[0].append(((64 * col_index),(64 * row_index),64,64))
						self.sprite_locations[1].append(((self.max_col * 64) - (64 * (col_index + 1)),(64 * row_index),64,64))
				if col == 'pu':
					for i in range(4):
						self.sprite_locations[2].append(((64 * col_index),(64 * row_index),64,64))
				if col == 'pd':
					for i in range(4):
						self.sprite_locations[3].append(((64 * col_index),(64 * row_index),64,64))
		
		print('player sprite setup complete' )

		
		#player attack animation
		self.attack_animation = False
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_2.png'), (12 * 64, 1 * 88)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_3.png'), (7 * 88, 1 * 64)))
		self.attack_sprite_locations = [[],[],[],[]]
		self.attack_max_row_1 = 8
		self.attack_max_col_1 = 10
		self.attack_max_row_2 = 8
		self.attack_max_col_2 = 7
		self.attack_counter = 0

		self.attack_spritesheet_mapping_1 = SAMPLE_2
		for row_index,row in enumerate(self.attack_spritesheet_mapping_1):
			for col_index, col in enumerate(row):
				if col == 'pu':
					for i in range(4):
						self.attack_sprite_locations[2].append(((64 * col_index),(64 * row_index),64,88))
				if col == 'pd':
					for i in range(4):
						self.attack_sprite_locations[3].append(((64 * col_index),(64 * row_index),64,88))
		self.attack_spritesheet_mapping_2 = SAMPLE_3
		for row_index,row in enumerate(self.attack_spritesheet_mapping_2):
			for col_index, col in enumerate(row):
				if col == 'pr':
					for i in range(3):
						self.attack_sprite_locations[0].append(((88 * col_index),(64 * row_index),88,64))
						self.attack_sprite_locations[1].append(((self.attack_max_col_2 * 88) - (88 * (col_index + 1)),(64 * row_index),88,64))

		#index value to get the image from the array
		#initially it is 0 
		# self.index = 0
		
		#now the image that we will display will be the index from the image array 
		self.image = self.images[0]

		#scale down
		# pygame.transform.scale(picture, (200, 200))

		#self.image = pygame.image.load('../graphics/test/link_sheet.png').convert_alpha().image_at((0, 0, 16, 16))
		#starting sprite
		self.sprite_location = self.sprite_locations[1][0]
		self.rect = self.image.get_rect(topleft = pos)

		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
		
		self.dynamic_offset = pygame.math.Vector2()
		self.dynamic_offset.x = 0
		self.dynamic_offset.y = 0
		# self.hitbox = self.rect.inflate(0,26)

		self.direction = pygame.math.Vector2()
		self.last_direction = 0
		self.speed = 5

		self.obstacle_sprites = obstacle_sprites
		self.attack = False
		#self.attack_clock = pygame.time.Clock()
		self.last_attack = pygame.time.get_ticks()
		self.attack_cooldown = 500
		self.able_to_attack = True
		self.attack_hitbox = self.rect.inflate(50,50)

		self.portals = portals
		self.parent = parent
		self.name = 'player'
		self.health = 10

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			# self.movement_counter_x = 0
			self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[2])
			self.direction.y = -1
			self.image = self.images[0]
			self.sprite_location =self.sprite_locations[2][self.movement_counter]
			self.last_direction = 2
		elif keys[pygame.K_DOWN]:
			# self.movement_counter_x = 0
			self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[3])
			self.direction.y = 1
			self.image = self.images[0]
			self.sprite_location =self.sprite_locations[3][self.movement_counter]
			self.last_direction = 3
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			# self.movement_counter_x = 0
			self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[0])
			self.direction.x = 1
		
			#finally we will update the image that will be displayed
			self.image = self.images[0]
			self.sprite_location =self.sprite_locations[0][self.movement_counter]
			self.last_direction = 0
		elif keys[pygame.K_LEFT]:
			# self.movement_counter_x = 0
			self.movement_counter = ( self.movement_counter + 1) % len(self.sprite_locations[1])
			self.direction.x = -1
		
			#finally we will update the image that will be displayed
			self.image = pygame.transform.flip(self.images[0],True,False)
			self.sprite_location = self.sprite_locations[1][self.movement_counter]
			self.last_direction = 1
		else:
			self.direction.x = 0
		if keys[pygame.K_SPACE]:
			#need to delay attacks
			if pygame.time.get_ticks() - self.attack_cooldown > self.last_attack:
				self.attack = True
				self.able_to_attack = False
				self.last_attack = pygame.time.get_ticks()
				# this needs to lock inputs until attack animation is complete
				self.attack_animation = True
				# set left attack offset
				if self.last_direction == 1:
					self.dynamic_offset.x = 24
				if self.last_direction == 2:
					self.dynamic_offset.y = 24

	def move(self,speed):

		if self.attack_animation == True:
			#all directions
			if self.attack_counter == len(self.attack_sprite_locations[self.last_direction]) - 1:
				self.attack_counter = 0
				self.attack_animation = False
				#need to display last dirction before attack
				if self.last_direction == 1:
					self.image = pygame.transform.flip(self.images[0],True,False)
				else:
					self.image = self.images[0]
				# reset attack offset
				self.dynamic_offset.x = 0
				self.dynamic_offset.y = 0
				self.sprite_location =self.sprite_locations[self.last_direction][self.movement_counter]
			else:
				if self.last_direction == 3 or self.last_direction == 2:
					self.image = self.images[1]
				if self.last_direction == 0:				
					self.image = self.images[2]
				if self.last_direction == 1:
					self.image = pygame.transform.flip(self.images[2],True,False)
				self.sprite_location =self.attack_sprite_locations[self.last_direction][self.attack_counter]
				self.attack_counter = self.attack_counter + 1

		else: 
			if self.direction.magnitude() != 0:
				self.direction = self.direction.normalize()

			self.hitbox.x += self.direction.x * speed
			self.attacked('horizontal')
			self.collision('horizontal', False)
			self.hitbox.y += self.direction.y * speed
			self.attacked('vertical')
			self.collision('vertical', False)
			self.rect.center = self.hitbox.center
		
			self.portal_collision()

			if self.attack:
				for sprite in self.obstacle_sprites:
					# attack general area sprite.hitbox.colliderect(Rect(self.hitbox.x - 20, self.hitbox.y - 20, self.hitbox.w + 40, self.hitbox.h + 40))
					if self.last_direction == 0:
						if sprite.hitbox.colliderect(Rect(self.hitbox.x + 32, self.hitbox.y - 32, self.hitbox.w + 32, self.hitbox.h + 64)) and sprite != self.rect :
							sprite.health -= 1
							print(sprite.health)
					if self.last_direction == 1:
						if sprite.hitbox.colliderect(Rect(self.hitbox.x - 64, self.hitbox.y - 32, self.hitbox.w + 32, self.hitbox.h + 64)) and sprite != self.rect :
							sprite.health -= 1
							print(sprite.health)
					if self.last_direction == 2:
						if sprite.hitbox.colliderect(Rect(self.hitbox.x - 32, self.hitbox.y - 64, self.hitbox.w + 64, self.hitbox.h + 32)) and sprite != self.rect :
							sprite.health -= 1
							print(sprite.health)
					if self.last_direction == 3:
						if sprite.hitbox.colliderect(Rect(self.hitbox.x - 32, self.hitbox.y + 32, self.hitbox.w + 64, self.hitbox.h + 32)) and sprite != self.rect :
							sprite.health -= 1
							print(sprite.health)
					if sprite.health <= 0:
						#log state of removed asset
						self.add_to_state(sprite)
						#remove sprite from physical groups
						sprite.kill()
				self.attack = False
		
	def attacked(self,direction):
		for sprite in self.obstacle_sprites:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				if sprite.name == 'spikes':
					self.health = self.health - 1
					#knockback
					for i in range(12):
						self.incremental_knockback(direction)
						self.collision(direction, True)
				if sprite.name == 'beartrap':
					self.health = self.health - 1
					self.add_to_state(sprite)
					sprite.kill()
					#knockback
					for i in range(12):
						self.incremental_knockback(direction)
						self.collision(direction, True)
				if sprite.name == 'thorny_plant':
					self.health = self.health - 1
					#knockback
					for i in range(12):
						self.incremental_knockback(direction)
						self.collision(direction, True)

	def collision(self,direction, is_knockback):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
					if ( self.direction.x > 0) != is_knockback: # and self.direction.x != 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if (self.direction.x < 0) != is_knockback: # and self.direction.x != 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
					if (self.direction.y > 0) != is_knockback: # and self.direction.y != 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if (self.direction.y < 0) != is_knockback: # and self.direction.y != 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def portal_collision(self):
		for sprite in self.portals:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				print("going to - ")
				print("level - " + sprite.next_map + " , sp - ")
				print(sprite.spawn_point)
				self.parent.parent.spawn  = (sprite.next_map,sprite.spawn_point, sprite.spawn_centering)
	
	# may be able to change 5 to a larger value
	def incremental_knockback(self,direction):
		if direction == 'vertical':
			if self.direction.y > 0: # moving down
				self.hitbox.top = self.hitbox.top - 5					
			if self.direction.y < 0: # moving up
				self.hitbox.top = self.hitbox.top + 5
		if direction == 'horizontal':
			if self.direction.x > 0: # moving right
				self.hitbox.left = self.hitbox.left - 5
			if self.direction.x < 0: # moving left
				self.hitbox.left = self.hitbox.left + 5	

	
	# add asset to changes state object
	def add_to_state(self,sprite):
		map_name = self.parent.spawn[0]
		change_state_x = round(sprite.pos[0] / 64)
		change_state_y = round(sprite.pos[1] / 64)
		change_state_name = str(change_state_x) + '_' + str(change_state_y) + '_' + sprite.name
		self.parent.parent.state_dictionary[map_name][change_state_name] = {}
		self.parent.parent.state_dictionary[map_name][change_state_name]['settings_grid_location'] = (change_state_x,change_state_y)
		self.parent.parent.state_dictionary[map_name][change_state_name]['state'] = 'killed'

	def update(self):
		self.input()
		self.move(self.speed)