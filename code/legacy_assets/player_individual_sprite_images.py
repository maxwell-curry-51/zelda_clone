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

		# # Create a black king.
		# b_king_rect = (68, 70, 85, 85)
		# b_king_image = piece_ss.image_at(b_king_rect)


		# ss = SpriteSheet('../graphics/test/link_sheet.png',1,1)
		# # Sprite is 16x16 pixels at location 0,0 in the file...
		# self.image = ss.image_at((0, 0, 16, 16))#adding all the images to sprite array
		self.images = []
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (1).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (2).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (3).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (4).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (5).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (6).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (7).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (8).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (9).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Walk (10).png'), (50, 50)))
		#index value to get the image from the array
		#initially it is 0 
		self.index = 0
		
		#now the image that we will display will be the index from the image array 
		self.image = self.images[self.index]

		#scale down
		# pygame.transform.scale(picture, (200, 200))

		#self.image = pygame.image.load('../graphics/test/link_sheet.png').convert_alpha().image_at((0, 0, 16, 16))
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,26)

		self.direction = pygame.math.Vector2()
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
		self.name = 'not floor'

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			#character animation
			#when the update method is called, we will increment the index
			self.index += 1
 
			#if the index is larger than the total images
			if self.index >= len(self.images):
				#we will make the index to 0 again
				self.index = 0
		
			#finally we will update the image that will be displayed
			self.image = self.images[self.index]
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			#character animation
			#when the update method is called, we will increment the index
			self.index += 1
 
			#if the index is larger than the total images
			if self.index >= len(self.images):
				#we will make the index to 0 again
				self.index = 0
		
			#finally we will update the image that will be displayed
			self.image = pygame.transform.flip(self.images[self.index],True,False)
		else:
			self.direction.x = 0
		if keys[pygame.K_SPACE]:
			#need to delay attacks
			# if self.able_to_attak:
			if pygame.time.get_ticks() - self.attack_cooldown > self.last_attack:
				self.attack = True
				self.able_to_attack = False
				self.last_attack = pygame.time.get_ticks()
		# if keys[pygame.K_1]:
		# 	#need to pause game
		# 	if pygame.time.get_ticks() - self.attack_cooldown > self.last_pause:
		# 		print('pause')
		# 		self.last_pause = pygame.time.get_ticks()
		# 		self.paused = not self.paused
		# 		self.parent.parent.paused = True

	def move(self,speed):

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center
		
		self.portal_collision()
		# if self.portal_collision():
		# 	#change level
		# 	print("change level")
		# 	# self.parent.background_image = '../graphics/dungeon/EP_1.png'
		# 	# self.parent.map = EP_1_MAP
		# 	# self.parent.create_map()

		# 	self.parent.parent.level_num  = 'ep_1'
			# self.parent.parent.background_image = '../graphics/dungeon/EP_1.png'
			# self.parent.parent.map = EP_1_MAP
		if self.attack:
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(Rect(self.hitbox.x - 20, self.hitbox.y - 20, self.hitbox.w + 20, self.hitbox.h + 20)) and sprite != self.rect :
					sprite.health -= 1
					print(sprite.health)
					#attack animation
			self.attack = False
		

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def portal_collision(self):
		for sprite in self.portals:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				print("going to - ")
				print("level - " + sprite.next_map + " , sp - ")
				print(sprite.spawn_point)
				# self.parent.parent.level_num  = 'ep_1'
				self.parent.parent.spawn  = (sprite.next_map,sprite.spawn_point, sprite.spawn_centering)
				#return True

	def update(self):
		self.input()
		self.move(self.speed)
