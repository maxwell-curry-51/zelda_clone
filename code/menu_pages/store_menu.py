import pygame 
from settings import *
from spritesheet import SpriteSheet


def Display_Store(display_surface):
	black_background = pygame.image.load('../graphics/maps/black_background.png')
	white = (255, 255, 255)
	black = (0, 0, 0)
	blue = (0, 0, 128)
	big_font = pygame.font.Font('freesansbold.ttf', 64)
	inventory_page_header_image = big_font.render('Merchant Store', True, white, black)
	inventory_page_header_rect = inventory_page_header_image.get_rect()
	# rect.center = (0, 0)
	# hitbox = pygame.Rect(rect.x,rect.y,64,64)
	display_surface.blit(black_background, (0, 0))
	display_surface.blit(inventory_page_header_image, ((1280 / 2) - inventory_page_header_rect.centerx, (720 / 2) - inventory_page_header_rect.centery))
	pygame.display.update()
