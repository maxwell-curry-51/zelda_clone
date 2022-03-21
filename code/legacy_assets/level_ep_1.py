import pygame 
from settings import *
from barriers.barrier import Barrier
from invisible_tile import InvisibleTile
from portal import Portal
from player import Player
from tracking_enemy import TrackingEnemy
from enemy import Enemy
from debug import debug

class LevelEP1:
	def __init__(self, parent, spawn, settings):

		self.parent = parent
		self.spawn = spawn
		self.map = settings[0] #use self.spawn[0]
		self.portal_mapping = settings[1]
		self.background_image = settings[2]

		self.background_image = '../graphics/dungeon/EP_1.png'
		self.map = EP_1_MAP #use self.spawn[0]
		self.portal_mapping = EP_1_PORTALS

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.player_sprite = pygame.sprite.Group()
		self.portals = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		portal_incrementor = 0
		sp_incrementor = 0
		for row_index,row in enumerate(self.map):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Barrier((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'i':
					InvisibleTile((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					if self.spawn[1] == sp_incrementor:
						self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.player_sprite, self.portals,self)
					sp_incrementor = sp_incrementor + 1
				if col == 'e':
					self.enemy = Enemy((x,y),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites)
				if col == 't':
					self.enemy = TrackingEnemy((x,y),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites,self.player_sprite)
				#portal mapping
				if col == 'd':
					self.enemy = Portal((x,y),[self.visible_sprites,self.portals],self.portal_mapping[portal_incrementor])
					portal_incrementor = portal_incrementor + 1

	def run(self):
		# update and draw the game

		#draw sprites
		self.visible_sprites.custom_draw(self.player, self.background_image)
		self.visible_sprites.update()
		#print(self.visible_sprites)


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player, background_image):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height
		
		#load map
		my_image = pygame.image.load(background_image)
		# Set the size for the image
		DEFAULT_IMAGE_SIZE = (3030, 3030)
		# Scale the image to your needed size
		image = pygame.transform.scale(my_image, DEFAULT_IMAGE_SIZE)
		#display map
		self.display_surface.blit(image, (-750,-900) - self.offset) # screen = pygame.display.set_mode((1200, 1000)) 

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
