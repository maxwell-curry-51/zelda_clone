import pygame 
from settings import *
from barriers.barrier import Barrier
from portal import Portal
from player import Player
from tracking_enemy import TrackingEnemy
from enemy import Enemy
from debug import debug

class SubLevel:
	def __init__(self, parent):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.player_sprite = pygame.sprite.Group()
		self.portals = pygame.sprite.Group()
		

		# sprite setup
		self.create_map()

		self.parent = parent

	def create_map(self):
		for row_index,row in enumerate(SUB_WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Barrier((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.player_sprite, self.portals, self)
				if col == 'e':
					self.enemy = Enemy((x,y),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites)
				if col == 't':
					self.enemy = TrackingEnemy((x,y),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites,self.player_sprite)
				if col == 'D':
					self.enemy = Portal((x,y),[self.visible_sprites,self.portals])

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
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

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
