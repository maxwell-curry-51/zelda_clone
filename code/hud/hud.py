import pygame 
from settings import *
from spritesheet import SpriteSheet


def Display_HUD(display_surface, health, max_hearts):
	# print(state_dictionary)
	# calculate totals
	# currency_count = 0
	# if level_name == "Village":
	# 	# print(state_dictionary["SAMPLE_VILLAGE_MAP"])
	# 	for object in state_dictionary["SAMPLE_VILLAGE_MAP"]:
	# 		# print(object)
	# 		if 'banana' in object:
	# 			currency_count += 1
	empty_heart = pygame.image.load('../graphics/hud/empty_heart.png')
	empty_heart_rect = empty_heart.get_rect()
	full_heart = pygame.image.load('../graphics/hud/full_heart.png')
	full_heart_rect = full_heart.get_rect()
	# white = (255, 255, 255)
	# black = (0, 0, 0)
	# blue = (0, 0, 128)
	# big_font = pygame.font.Font('freesansbold.ttf', 64)
	# smaller_font = pygame.font.Font('freesansbold.ttf', 32)
	# level_name_image = big_font.render('HUD', True, white, black)
	# level_name_rect = level_name_image.get_rect()
	# next_level_image = smaller_font.render('Next Level', True, white, black)
	# next_level_rect = next_level_image.get_rect()
	# previous_name_image = smaller_font.render('Previous Level', True, white, black)
	# previous_name_rect = previous_name_image.get_rect()
	# currency_count_image = smaller_font.render(str(currency_count), True, white, black)
	# currency_count_rect = previous_name_image.get_rect()
	# currency_type_image = smaller_font.render('Currency', True, white, black)
	# currency_type_rect = previous_name_image.get_rect()
	# rect.center = (0, 0)
	# hitbox = pygame.Rect(rect.x,rect.y,64,64)

	for i in range(max_hearts):
		if i < health:
			display_surface.blit(full_heart, ((1280) - ( 2 * i * empty_heart_rect.centerx )  ,10))
		else:
			display_surface.blit(empty_heart, ((1280) - ( 2 * i * empty_heart_rect.centerx ) ,10))

	# display_surface.blit(black_background, (0, 0))
	# display_surface.blit(level_name_image, ((1280 / 2) - level_name_rect.centerx, level_name_rect.centery))
	# display_surface.blit(next_level_image, ((1280) - next_level_rect.centerx ,0))
	# display_surface.blit(next_level_image, ((1280) - next_level_rect.centerx ,0))
	# display_surface.blit(previous_name_image, (0, 0))
	# display_surface.blit(currency_count_image, ((1280 / 2) - currency_count_rect.centerx, (720 / 2) - currency_count_rect.centery))
	# display_surface.blit(currency_type_image, ((1280 / 2) + currency_type_rect.centerx, (720 / 2) - currency_type_rect.centery))
	pygame.display.update()
