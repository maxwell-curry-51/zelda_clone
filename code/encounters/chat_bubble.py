import pygame 
from pygame.locals import *
from settings import *

class ChatBubble(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)

		self.image_raw = pygame.image.load('../graphics/png/chat_bubble.png').convert_alpha()
		self.image = pygame.transform.scale(self.image_raw, (200,200))
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = pygame.Rect(self.rect.x,self.rect.y,64,64)
		self.remove = False
		self.name = 'chat_bubble'

		self.visible = False
		self.offset = pygame.math.Vector2()
		self.offset.x = 0
		self.offset.y = 0

		self.chat_offset = pygame.math.Vector2()
		self.chat_offset.x = -self.rect.width /4
		self.chat_offset.y = -self.rect.height /2
		
		self.health = float('inf')
