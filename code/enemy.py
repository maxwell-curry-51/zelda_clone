import pygame 
from settings import *
from spritesheet import SpriteSheet


class Enemy(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		#boundary box for movement
		super().__init__(groups)
		
		# used for state management
		self.pos = pos
		
		self.remove = False

		#adding all the images to sprite array
		self.images = []
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (1).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (2).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (3).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (4).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (5).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (6).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (7).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (8).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (9).png'), (50, 50)))
		self.images.append(pygame.transform.scale(pygame.image.load('../graphics/png/Dead (10).png'), (50, 50)))

		self.path = []
		for i in range(1,25):
			self.path.append(1)
		for i in range(1,25):
			self.path.append(2)
		for i in range(1,25):
			self.path.append(3)
		for i in range(1,25):
			self.path.append(4)
		self.path_index = 0

		
		self.delay = []
		for i in range(1,5):
			self.delay.append(0)
		self.delay.append(1)
		self.delay_index = 0
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
		
		self.health = 5
		self.name = 'not floor'

	def input(self):
		#get player location
		if self.path[self.path_index] == 4:
			self.direction.y = -1
			#if the index is larger than the total images
			if self.path_index >= len(self.path) - 1:
				#we will make the index to 0 again
				self.path_index = 0
		elif self.path[self.path_index] == 2:
			self.direction.y = 1
		elif self.path[self.path_index] == 1:
			self.direction.x = 1
		elif self.path[self.path_index] == 3:
			self.direction.x = -1
		else:
			self.direction.x = 0
			self.direction.y = 0
		self.path_index += 1

	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center
		self.direction.x = 0
		self.direction.y = 0
		

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

	def update(self):
		
		if self.health <= 0:
			#remove sprite from physical groups
			self.kill()

		if self.delay[self.delay_index] == 1:
			self.input()
			self.move(self.speed)
			self.delay_index = 0
		self.delay_index += 1
		#character animation
		#when the update method is called, we will increment the index
		# self.index += 1
 
		#if the index is larger than the total images
		if self.index >= len(self.images):
			#we will make the index to 0 again
			self.index = 0
		
		#finally we will update the image that will be displayed
		self.image = self.images[self.index]