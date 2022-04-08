import pygame 
from settings import *
from spritesheet import SpriteSheet


def Display_Startup_Erase_Or_Play_Menu(display_surface, character_selected, erase_or_play_option_highlighted):
	black_background = pygame.image.load('../graphics/maps/black_background.png')
	white = (255, 255, 255)
	black = (0, 0, 0)
	grey = (128, 128, 128)
	big_font = pygame.font.Font('freesansbold.ttf', 64)
	character_pre_load_header_image = big_font.render('Character Select Screen', True, white, black)
	character_pre_load_header_rect = character_pre_load_header_image.get_rect()
	character_pre_load_name_image = big_font.render(character_selected + ' - selected', True, white, black)
	character_pre_load_name_rect = character_pre_load_name_image.get_rect()
	if erase_or_play_option_highlighted == 0:
		character_pre_load_play_image = big_font.render('Play', True, white, black)
		character_pre_load_erase_image = big_font.render('Erase Character', True, grey, black)
	else:
		character_pre_load_play_image = big_font.render('Play', True, grey, black)
		character_pre_load_erase_image = big_font.render('Erase Character', True, white, black)
	character_pre_load_play_rect = character_pre_load_play_image.get_rect()
	character_pre_load_erase_rect = character_pre_load_erase_image.get_rect()
	# rect.center = (0, 0)
	# hitbox = pygame.Rect(rect.x,rect.y,64,64)
	display_surface.blit(black_background, (0, 0))
	display_surface.blit(character_pre_load_header_image, ((1280 / 2) - character_pre_load_header_rect.centerx, (720 / 2) - character_pre_load_header_rect.centery))
	display_surface.blit(character_pre_load_name_image, ((1280 / 2) - character_pre_load_name_rect.centerx, ((720 / 2) - character_pre_load_name_rect.centery) + 64))
	display_surface.blit(character_pre_load_play_image, ((1280 / 2) - character_pre_load_play_rect.centerx, ((720 / 2) - character_pre_load_play_rect.centery) + 128))
	display_surface.blit(character_pre_load_erase_image, ((1280 / 2) - character_pre_load_erase_rect.centerx, ((720 / 2) - character_pre_load_erase_rect.centery) + 196))
	pygame.display.update()
