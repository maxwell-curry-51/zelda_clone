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