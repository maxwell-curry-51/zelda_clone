import pygame 
from settings import *
from spritesheet import SpriteSheet


def Display_Startup_Character_Select_Menu(display_surface, character_list, player_highlighted):
	black_background = pygame.image.load('../graphics/maps/black_background.png')
	white = (255, 255, 255)
	black = (0, 0, 0)
	grey = (128, 128, 128)
	big_font = pygame.font.Font('freesansbold.ttf', 64)
	character_select_header_image = big_font.render('Character Select Screen', True, white, black)
	character_select_header_rect = character_select_header_image.get_rect()
	if player_highlighted == 0:
		character_select_save_file_1_image = big_font.render(character_list[0], True, white, black)
	else:
		character_select_save_file_1_image = big_font.render(character_list[0], True, grey, black)
	if player_highlighted == 1:
		character_select_save_file_2_image = big_font.render(character_list[1], True, white, black)
	else:
		character_select_save_file_2_image = big_font.render(character_list[1], True, grey, black)
	if player_highlighted == 2:
		character_select_save_file_3_image = big_font.render(character_list[2], True, white, black)
	else:
		character_select_save_file_3_image = big_font.render(character_list[2], True, grey, black)
	character_select_save_file_1_rect = character_select_save_file_1_image.get_rect()
	character_select_save_file_2_rect = character_select_save_file_2_image.get_rect()
	character_select_save_file_3_rect = character_select_save_file_3_image.get_rect()
	display_surface.blit(black_background, (0, 0))
	display_surface.blit(character_select_header_image, ((1280 / 2) - character_select_header_rect.centerx, (720 / 2) - character_select_header_rect.centery))
	display_surface.blit(character_select_save_file_1_image, ((1280 / 2) - character_select_save_file_1_rect.centerx, ((720 / 2) - character_select_header_rect.centery) + 64))
	display_surface.blit(character_select_save_file_2_image, ((1280 / 2) - character_select_save_file_2_rect.centerx, ((720 / 2) - character_select_header_rect.centery) + 128))
	display_surface.blit(character_select_save_file_3_image, ((1280 / 2) - character_select_save_file_3_rect.centerx, ((720 / 2) - character_select_header_rect.centery) + 196))
	pygame.display.update()
