import pygame 
from barriers.barrier import Barrier
from barriers.barrier_tl import BarrierTL
from barriers.barrier_tr import BarrierTR
from barriers.barrier_br import BarrierBR
from barriers.barrier_bl import BarrierBL
from floor_tile import FloorTile
from invisible_tile import InvisibleTile
from portal import Portal
from player import Player
from enemies.enemy import Enemy
from enemies.spikes import Spikes
from enemies.beartrap import BearTrap
from enemies.thorny_plant import ThornyPlant
from tracking_enemy import TrackingEnemy
from allies.npc_ally import NPCAlly
from encounters.chat_bubble import ChatBubble
from encounters.chat_bubble_text import ChatBubbleText
from debug import debug

class Level:
	def __init__(self, parent, spawn, settings):
		self.debug = False

		self.parent = parent
		self.spawn = spawn
		self.removed_assets = []
		#need to load state from previous entries into this level if exists
		if self.spawn[0] in parent.state_dictionary.keys():
			# load from state
			for asset in parent.state_dictionary[self.spawn[0]]:
				self.removed_assets.append(parent.state_dictionary[self.spawn[0]][asset]['settings_grid_location'])
		else:
			#create new state object for this level
			parent.state_dictionary[self.spawn[0]] = {}

		
		self.map = settings[0] #use self.spawn[0]
		self.portal_mapping = settings[1]
		self.background_image = pygame.image.load(settings[2])
		self.tilesize = settings[3]
		self.image_size = settings[4]
		self.image_shift = settings[5]

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup(self.image_size,self.image_shift)
		self.obstacle_sprites = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		self.ally_sprites = pygame.sprite.Group()
		self.player_sprite = pygame.sprite.Group()
		self.portals = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		portal_incrementor = 0
		sp_incrementor = 0
		ChatBubble((500,500),[self.visible_sprites,self.ally_sprites])
		ChatBubbleText((500,500),[self.visible_sprites,self.ally_sprites],0)
		ChatBubbleText((500,500),[self.visible_sprites,self.ally_sprites],1)
		ChatBubbleText((500,500),[self.visible_sprites,self.ally_sprites],2)
		ChatBubbleText((500,500),[self.visible_sprites,self.ally_sprites],3)
		for row_index,row in enumerate(self.map):
			for col_index, col in enumerate(row):
				#make sure asset has not been removed
				if (col_index, row_index) not in self.removed_assets: #this is not the really slow step
					x = col_index * self.tilesize
					y = row_index * self.tilesize
					if col == ' ':
						pass
					elif col == 'x':
						Barrier((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == 'l':
						BarrierTL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == 'r':
						BarrierTR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == 't':
						BarrierTL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierTR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == 'b':
						BarrierBL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '0':
						BarrierTL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '1':
						BarrierTR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '2':
						BarrierBL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '3':
						BarrierBR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '4':
						BarrierTL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierTR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '5':
						BarrierTL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierTR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '6':
						BarrierTL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == '7':
						BarrierTR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBL((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
						BarrierBR((x,y),[self.visible_sprites,self.obstacle_sprites],self.debug)
					elif col == 'f':
						FloorTile((x,y),[self.visible_sprites])
					elif col == 'i':
						InvisibleTile((x,y),[self.visible_sprites,self.obstacle_sprites])
					elif col == 'p':
						if self.spawn[1] == sp_incrementor:
							# centering player to the door
							if self.spawn[2] == 'm':
								self.player = Player((x + 32,y),[self.visible_sprites,self.obstacle_sprites,self.player_sprite],self.obstacle_sprites,self.player_sprite, self.enemy_sprites, self.ally_sprites, self.portals,self)
							else:
								self.player = Player((x ,y),[self.visible_sprites,self.obstacle_sprites,self.player_sprite],self.obstacle_sprites,self.player_sprite, self.enemy_sprites, self.ally_sprites, self.portals,self)
						sp_incrementor = sp_incrementor + 1
					elif col == 'e':
						Enemy((x,y),[self.visible_sprites,self.enemy_sprites],self.obstacle_sprites)
					elif col == 's':
						Spikes((x,y),[self.visible_sprites,self.obstacle_sprites, self.enemy_sprites])
					elif col == '*':
						BearTrap((x,y),[self.visible_sprites,self.obstacle_sprites, self.enemy_sprites])
					elif col == '+':
						ThornyPlant((x,y),[self.visible_sprites,self.obstacle_sprites, self.enemy_sprites])
					elif col == 'h':
						TrackingEnemy((x,y),[self.visible_sprites, self.enemy_sprites],self.obstacle_sprites,self.player_sprite)
					elif col == 'n':
						NPCAlly((x,y),[self.visible_sprites,self.obstacle_sprites, self.ally_sprites])
					# elif col == 'c':
					# 	ChatBubble((x,y),[self.visible_sprites,self.obstacle_sprites])
					#portal mapping
					elif col == 'd':
						print(portal_incrementor)
						Portal((x,y),[self.visible_sprites,self.portals],self.portal_mapping[portal_incrementor])
						portal_incrementor = portal_incrementor + 1

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player, self.background_image)
		self.visible_sprites.update()



class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self,image_size,image_shift):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()
		self.static_player_offset = pygame.math.Vector2()
		self.image_size = image_size
		self.image_shift = image_shift

	def custom_draw(self,player, background_image):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height
		self.static_player_offset.x = player.rect.left - self.half_width + 32
		self.static_player_offset.y = player.rect.top - self.half_height + 32
		
		#load map
		my_image = background_image
		# Set the size for the image
		# DEFAULT_IMAGE_SIZE = (2700, 2500)
		# Scale the image to your needed size
		image = pygame.transform.scale(my_image, self.image_size)
		#display map
		self.display_surface.blit(image, self.image_shift - self.offset) # screen = pygame.display.set_mode((1200, 1000)) 

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			offset_pos_right = sprite.rect.topright - self.offset
			offset_pos_bottom = sprite.rect.bottomleft - self.offset
			offset_pos_bottom_right = sprite.rect.bottomright - self.offset
			offset_pos_bottom_left = sprite.rect.bottomleft - self.offset
			# self.display_surface.blit(sprite.image,offset_pos)
			if sprite.name == 'floor':
				self.display_surface.blit(sprite.image, offset_pos, sprite.sprite_location)
			elif sprite.name == 'spikes':
				self.display_surface.blit(sprite.image, offset_pos, sprite.sprite_location)
			elif sprite.name == 'beartrap':
				self.display_surface.blit(sprite.image, offset_pos, sprite.sprite_location)
			elif sprite.name == 'thorny_plant':
				self.display_surface.blit(sprite.image, offset_pos, sprite.sprite_location)
			elif sprite.name == 'npc_ally':
				self.display_surface.blit(sprite.image, offset_pos, sprite.sprite_location)
			elif sprite.name == 'enemy':
				player_offest =  sprite.rect.topleft - self.static_player_offset - sprite.dynamic_offset
				self.display_surface.blit(sprite.image, player_offest, sprite.sprite_location)
			elif sprite.name == 'player':
				player_offest =  sprite.rect.topleft - self.static_player_offset - sprite.dynamic_offset
				self.display_surface.blit(sprite.image, player_offest, sprite.sprite_location)
			elif sprite.name == 'right':
				self.display_surface.blit(sprite.image, offset_pos_right)
			elif sprite.name == 'bottom':
				self.display_surface.blit(sprite.image, offset_pos_bottom)
			elif sprite.name == 'bottom_right':
				self.display_surface.blit(sprite.image, offset_pos_bottom_right)
			elif sprite.name == 'bottom_left':
				self.display_surface.blit(sprite.image, offset_pos_bottom_left)
			elif sprite.name == 'chat_bubble':
				if sprite.visible:
					self.display_surface.blit(sprite.image, sprite.offset - self.offset)
			else:
				self.display_surface.blit(sprite.image,offset_pos)
		#must draw speech text last
		for sprite in self.sprites():
			if sprite.name == 'chat_bubble_text':
				if sprite.visible:
					print('visible')
					self.display_surface.blit(sprite.image, sprite.offset - self.offset)
