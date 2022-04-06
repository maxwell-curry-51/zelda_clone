import pygame 
from pygame.locals import *
from settings import *

class ChatBubbleText(pygame.sprite.Sprite):
	def __init__(self,pos,groups, line_number):
		super().__init__(groups)
		white = (255, 255, 255)
		black = (0, 0, 0)
		blue = (0, 0, 128)

		font = pygame.font.Font('freesansbold.ttf', 16)
		self.image = font.render('', True, black, white)
		self.rect = self.image.get_rect()
		self.rect.center = (100, 100)
		
		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
		self.remove = False
		self.name = 'chat_bubble_text'

		self.line_number = line_number

		self.visible = False
		self.offset = pygame.math.Vector2()
		self.offset.x = 0
		self.offset.y = 0

		self.chat_offset = pygame.math.Vector2()
		self.chat_offset.x = (-self.rect.width /4)
		self.chat_offset.y = -self.rect.height /2
		
		self.health = float('inf')

	def render_new_speech_bubble(self, text):
		white = (255, 255, 255)
		black = (0, 0, 0)
		blue = (0, 0, 128)
		font = pygame.font.Font('freesansbold.ttf', 16)
		self.image = font.render(text, True, black, white)
		self.rect = self.image.get_rect()
		self.rect.center = (100, 100)
		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
