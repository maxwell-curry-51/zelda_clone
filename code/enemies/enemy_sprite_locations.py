
from settings import *
import pygame
IMAGES = []
IMAGES.append(pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64)))
IMAGE = pygame.transform.scale(pygame.image.load('../graphics/player_sprites/sample_1.png'), (10 * 64, 8 * 64))
SPRITE_LOCATIONS = [[],[],[],[]]
MAX_ROW = 8
MAX_COL = 10
for row_index,row in enumerate(SAMPLE_1):
	for col_index, col in enumerate(row):
		if col == 'er':
			for i in range(6):
				SPRITE_LOCATIONS[0].append(((64 * col_index),(64 * row_index),64,64))
				SPRITE_LOCATIONS[1].append(((MAX_COL * 64) - (64 * (col_index + 1)),(64 * row_index),64,64))
		if col == 'eu':
			for i in range(12):
				SPRITE_LOCATIONS[2].append(((64 * col_index),(64 * row_index),64,64))
		if col == 'ed':
			for i in range(6):
				SPRITE_LOCATIONS[3].append(((64 * col_index),(64 * row_index),64,64))
