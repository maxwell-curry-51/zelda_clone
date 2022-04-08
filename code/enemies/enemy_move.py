def move(self):
	if self.attacked:
		if self.attacked_incrementor < 20:
			incremental_knockback(self)
			self.rect.center = self.hitbox.center
			self.attacked_incrementor = self.attacked_incrementor + 1
		else:
			self.attacked_incrementor = 0
			self.attacked = False
	else:
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()	

		self.hitbox.x += self.direction.x * self.speed
		collision(self, 'horizontal',False)
		self.hitbox.y += self.direction.y * self.speed
		collision(self, 'vertical', False)
		self.rect.center = self.hitbox.center
		self.direction.x = 0
		self.direction.y = 0

def collision(self,direction, is_knockback):
	if direction == 'horizontal':
		for sprite in self.obstacle_sprites:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				if ( self.direction.x > 0) != is_knockback: # and self.direction.x != 0: # moving right
					self.hitbox.right = sprite.hitbox.left
				if (self.direction.x < 0) != is_knockback: # and self.direction.x != 0: # moving left
					self.hitbox.left = sprite.hitbox.right

	if direction == 'vertical':
		for sprite in self.obstacle_sprites:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				if (self.direction.y > 0) != is_knockback: # and self.direction.y != 0: # moving down
					self.hitbox.bottom = sprite.hitbox.top
				if (self.direction.y < 0) != is_knockback: # and self.direction.y != 0: # moving up
					self.hitbox.top = sprite.hitbox.bottom


def knockback_collision(self,direction, is_knockback):
	if direction == 'horizontal':
		for sprite in self.obstacle_sprites:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				if ( self.attack_direction.x > 0): # and self.direction.x != 0: # moving right
					self.hitbox.left = sprite.hitbox.right
				if (self.attack_direction.x < 0): # and self.direction.x != 0: # moving left
					self.hitbox.right = sprite.hitbox.left

	if direction == 'vertical':
		for sprite in self.obstacle_sprites:
			if sprite.hitbox.colliderect(self.hitbox) and sprite != self.rect :
				if (self.attack_direction.y > 0): # and self.direction.y != 0: # moving down
					self.hitbox.top = sprite.hitbox.bottom
				if (self.attack_direction.y < 0): # and self.direction.y != 0: # moving up
					self.hitbox.bottom = sprite.hitbox.top
					
# MOVEMENT_DELAY = [0,1]
def incremental_knockback(self):
	if self.attack_direction.y > 0: # moving down
		self.hitbox.top = self.hitbox.top - 5					
	if self.attack_direction.y < 0: # moving up
		self.hitbox.top = self.hitbox.top + 5
	knockback_collision(self, 'vertical', True)
	if self.attack_direction.x > 0: # attack pushes left
		self.hitbox.left = self.hitbox.left - 5
	if self.attack_direction.x < 0: # attack pushes right
		self.hitbox.left = self.hitbox.left + 5	
	knockback_collision(self, 'horizontal',True)
