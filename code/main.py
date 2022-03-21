import pygame, sys
from pygame.locals import *
from settings import *
# from level import Level
# from sublevel import SubLevel
from level_ep_0 import LevelEP0
# from level_ep_1 import LevelEP1

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		#pause menu
		self.paused = False
		self.pause_menu_selected = 0
		self.up_released = True
		self.down_released = True
		self.pause_released = True

		# self.last_level_num = 'ep_0'
		# self.level_num = 'ep_0'
		self.last_spawn = ('EP_0_MAP',3,'m')
		self.spawn = ('EP_0_MAP',3,'m')

		#state object
		'''
		this state_dictionary will hold all level information, maybe in a form like
		this also could be used for calculating totals where:
		  may need one for respawnables (session based)
		  may need one for collectables (map changed forever) <- this is what we will implement first
		{
			'level_name': {
				'altered_asset_1' : {
					'settings_grid_location' : (3,7),
					'state' : 'killed'
				},
				'altered_asset_2' : {
					'settings_grid_location' : (4,4),
					'state' : 'found'
				}
			}
		}
		'''
		self.state_dictionary = {}

		self.Load_Level()
	
	def run(self):
		display_surface = pygame.display.get_surface()
		while True:
			keys = pygame.key.get_pressed()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			#button events
			#pause menu controls
			if self.paused:
				if keys[pygame.K_UP]:
					if self.up_released:
						self.Display_Pause_Menu(display_surface, self.pause_menu_selected)
						self.pause_menu_selected = (self.pause_menu_selected - 1) % 3
						self.up_released = False
				elif keys[pygame.K_DOWN]:
					if self.down_released:
						self.Display_Pause_Menu(display_surface, self.pause_menu_selected)
						self.pause_menu_selected = (self.pause_menu_selected + 1) % 3
						self.down_released = False
				else:
					self.up_released = True
					self.down_released = True
			#global buttons - will override player buttons
			if keys[pygame.K_1]:
				if self.pause_released:
					if self.paused and self.pause_menu_selected == 0:
						self.Display_Pause_Menu(display_surface, self.pause_menu_selected)
						print('unpaused')
						self.paused = False
						self.pause_menu_selected = 0
					else:
						print('paused')
						self.paused = True
					self.pause_released = False
			else:
				self.pause_released = True

			if self.paused:
				self.Display_Pause_Menu(display_surface, self.pause_menu_selected)
			else:
				self.screen.fill('black')
				self.level.run()
				pygame.display.update()
				self.clock.tick(FPS)
				if self.last_spawn[0] != self.spawn[0]:
					self.last_spawn = self.spawn
					self.Load_Level()

	def Load_Level(self):
		self.level = LevelEP0(self, self.spawn, SETTINGS[SETTING_INDEXES.index(self.spawn[0])])
	
	def Display_Pause_Menu(self,display_surface,pause_menu_selected):
		pause_background = pygame.image.load('../graphics/pause_menu/pause_background.png')
		pause_selection_background = pygame.image.load('../graphics/pause_menu/pause_selection_background.png')
		return_to_game_unselected = pygame.image.load('../graphics/pause_menu/return_to_game_unselected.png')
		return_to_game_selected = pygame.image.load('../graphics/pause_menu/return_to_game_selected.png')
		display_surface.blit(pause_background, (0,0))
		display_surface.blit(pause_selection_background, (120,180))
		display_surface.blit(pause_selection_background, (120,300))
		display_surface.blit(pause_selection_background, (120,420))
		if pause_menu_selected == 0:
			display_surface.blit(return_to_game_selected, (120,180))
			display_surface.blit(return_to_game_unselected, (120,300))
			display_surface.blit(return_to_game_unselected, (120,420))
		if pause_menu_selected == 1:
			display_surface.blit(return_to_game_unselected, (120,180))
			display_surface.blit(return_to_game_selected, (120,300))
			display_surface.blit(return_to_game_unselected, (120,420))
		if pause_menu_selected == 2:
			display_surface.blit(return_to_game_unselected, (120,180))
			display_surface.blit(return_to_game_unselected, (120,300))
			display_surface.blit(return_to_game_selected, (120,420))
		pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()