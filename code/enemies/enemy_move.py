from collision import * 

def move(self):
	if self.attacked:
		print('attacked')
		if self.attacked_incrementor < 20:
			print('moving')
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

# MOVEMENT_DELAY = [0,1]
def incremental_knockback(self):
	if self.attack_direction.y > 0: # moving down
		self.hitbox.top = self.hitbox.top - 5					
	if self.attack_direction.y < 0: # moving up
		self.hitbox.top = self.hitbox.top + 5
	collision(self, 'vertical', True)
	if self.attack_direction.x > 0: # moving right
		self.hitbox.left = self.hitbox.left - 5
	if self.attack_direction.x < 0: # moving left
		self.hitbox.left = self.hitbox.left + 5	
	collision(self, 'horizontal',True)
