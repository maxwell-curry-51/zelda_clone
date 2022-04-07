import pygame, sys
from pygame.locals import *
from settings import *
import time
from level import Level
from menu_pages.pause_menu import *
from menu_pages.stats_menu import *
from menu_pages.inventory_menu import *
from menu_pages.map_menu import *
from menu_pages.skill_tree_menu import *
from menu_pages.store_menu import *

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		#pause menu
		self.paused = False
		self.in_menu = False
		self.in_store = False
		self.pause_menu_option_selected = 0
		self.level_name = ["Village", "Forest", "City Ruins", "Whitish Castle", "Catacombs", "Hell", "The Simulation"]
		self.dungeon_level_name = ["Village Dungeon", "Forest Dungeon", "City Ruins Dungeon", "Whitish Castle Dungeon", "Catacombs Dungeon", "Hell Dungeon", "The Simulation Dungeon"]
		self.stats_page_level_selected = 0
		self.stats_page_dungeon_selected = False
		
		#button toggles
		self.up_button_released = True
		self.down_button_released = True
		self.pause_button_released = True
		self.a_button_released = True
		self.b_button_released = True
		self.rb_button_released = True
		self.lb_button_released = True
		self.x_button_released = True
		self.pause_menu_page = 0
		self.inventory_menu_page = 0
		
		self.changed = False
		self.last_spawn = ('SAMPLE_VILLAGE_MAP',1,'m')
		self.spawn = ('SAMPLE_VILLAGE_MAP',1,'m')

		#state object
		'''
		*******probably chould add another level for 'level'
			level -> map -> objects killed/ found
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
		#load player profile from state
		self.player_health = 8

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
				if keys[pygame.K_UP]: # navigate menu
					if self.up_button_released:
						if self.pause_menu_page == 0:
							self.pause_menu_option_selected = (self.pause_menu_option_selected - 1) % 3
						self.up_button_released = False
				elif keys[pygame.K_DOWN]: # navigate menu
					if self.down_button_released:
						if self.pause_menu_page == 0:
							self.pause_menu_option_selected = (self.pause_menu_option_selected + 1) % 3
						self.down_button_released = False
				elif keys[pygame.K_a]: # accept highlighted option if avaliable
					if self.a_button_released:
						if self.pause_menu_option_selected == 0:
							self.paused = False
						elif self.pause_menu_option_selected == 1:
							self.pause_menu_page = 1
						self.a_button_released = False
				elif keys[pygame.K_b]: # go back 1 menu page
					if self.b_button_released:
						if self.pause_menu_page == 0:
							self.paused = False
						elif self.pause_menu_page == 1:
							self.pause_menu_page = 0
						self.b_button_released = False
				elif keys[pygame.K_r]: # flip pages in stats menu
					if self.rb_button_released:
						if self.pause_menu_page == 1:
							if self.stats_page_level_selected < len(self.level_name) - 1:
								self.stats_page_level_selected += 1
						self.rb_button_released = False
				elif keys[pygame.K_l]: # flip pages in stats menu
					if self.lb_button_released:
						if self.pause_menu_page == 1:
							if self.stats_page_level_selected > 0:
								self.stats_page_level_selected -= 1
						self.lb_button_released = False
				elif keys[pygame.K_x]: # toggle dungeon in stats menu
					if self.x_button_released:
						if self.pause_menu_page == 1:
							self.stats_page_dungeon_selected = not self.stats_page_dungeon_selected
						self.x_button_released = False
				else:
					self.up_button_released = True
					self.down_button_released = True
					self.a_button_released = True
					self.b_button_released = True
					self.rb_button_released = True
					self.lb_button_released = True
					self.x_button_released = True
			#inventory menu controls
			if self.in_menu:
				if keys[pygame.K_b]: # go back 1 menu page
					if self.b_button_released:
						self.in_menu = False
						self.b_button_released = False
				elif keys[pygame.K_x]: # toggle inventory / skill tree menu
					if self.x_button_released:
						self.inventory_menu_page = (self.inventory_menu_page + 1) % 3
						self.x_button_released = False
				else:
					self.up_button_released = True
					self.down_button_released = True
					self.a_button_released = True
					self.b_button_released = True
					self.rb_button_released = True
					self.lb_button_released = True
					self.x_button_released = True
			if self.in_store:
				if keys[pygame.K_b]: # go back 1 menu page
					if self.b_button_released:
						self.in_store = False
						self.b_button_released = False
				else:
					self.up_button_released = True
					self.down_button_released = True
					self.a_button_released = True
					self.b_button_released = True
					self.rb_button_released = True
					self.lb_button_released = True
					self.x_button_released = True
			#global buttons - will override player buttons
			if keys[pygame.K_1] and not self.in_menu and not self.in_store: # start_button -> pause menu
				if self.pause_button_released:
					if self.paused:
						self.paused = False
						self.pause_menu_option_selected = 0
					else:
						self.paused = True
						self.pause_menu_page = 0
					self.pause_button_released = False
			elif keys[pygame.K_2] and not self.paused and not self.in_store: #  select_button -> inventory menu
				if self.select_button_released:
					if self.in_menu:
						self.in_menu = False
					else:
						self.in_menu = True
						self.select_menu_page = 0
					self.select_button_released = False
			else:
				self.pause_button_released = True
				self.select_button_released = True

			if self.paused:
				if self.pause_menu_page == 0:
					Display_Pause_Menu(display_surface, self.pause_menu_option_selected)
				if self.pause_menu_page == 1:
					if self.stats_page_dungeon_selected:
						Display_Stats_Menu(display_surface, self.dungeon_level_name[self.stats_page_level_selected], self.state_dictionary)
					else:						
						Display_Stats_Menu(display_surface, self.level_name[self.stats_page_level_selected], self.state_dictionary)
			elif self.in_menu:
					if self.inventory_menu_page == 0:
						Display_Inventory_Menu(display_surface)
					elif self.inventory_menu_page == 1:
						Display_Skill_Tree_Menu(display_surface)
					elif self.inventory_menu_page == 2:
						Display_Map_Menu(display_surface)
			elif self.in_store:
				Display_Store(display_surface)
			else:
				if self.last_spawn[0] != self.spawn[0]:
					self.last_spawn = self.spawn
					self.Load_Level()
					self.changed = True
				self.screen.fill('black')
				self.level.run()
				#shitty fix because update renders one frame incorrectly
				if self.changed:
					self.screen.fill('black')
				pygame.display.update()
				self.clock.tick(FPS)
				if self.changed == True:
					self.changed = False



	def Load_Level(self):
		self.level = Level(self, self.spawn, SETTINGS[SETTING_INDEXES.index(self.spawn[0])])
	

if __name__ == '__main__':
	game = Game()
	game.run()
