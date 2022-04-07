import pygame 
from settings import *
from spritesheet import SpriteSheet


def Display_Pause_Menu(display_surface,pause_menu_option_selected):
	black_background = pygame.image.load('../graphics/maps/black_background.png')
	display_surface.blit(black_background, (0, 0))
	pause_background = pygame.image.load('../graphics/pause_menu/pause_background.png')
	pause_selection_background = pygame.image.load('../graphics/pause_menu/pause_selection_background.png')
	return_to_game_unselected = pygame.image.load('../graphics/pause_menu/return_to_game_unselected.png')
	return_to_game_selected = pygame.image.load('../graphics/pause_menu/return_to_game_selected.png')
	display_surface.blit(pause_background, (0,0))
	display_surface.blit(pause_selection_background, (120,180))
	display_surface.blit(pause_selection_background, (120,300))
	display_surface.blit(pause_selection_background, (120,420))
	if pause_menu_option_selected == 0:
		display_surface.blit(return_to_game_selected, (120,180))
		display_surface.blit(return_to_game_unselected, (120,300))
		display_surface.blit(return_to_game_unselected, (120,420))
	if pause_menu_option_selected == 1:
		display_surface.blit(return_to_game_unselected, (120,180))
		display_surface.blit(return_to_game_selected, (120,300))
		display_surface.blit(return_to_game_unselected, (120,420))
	if pause_menu_option_selected == 2:
		display_surface.blit(return_to_game_unselected, (120,180))
		display_surface.blit(return_to_game_unselected, (120,300))
		display_surface.blit(return_to_game_selected, (120,420))
	pygame.display.update()
