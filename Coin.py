import pygame

class Coin():
	
	size = 100
	image = pygame.image.load('coin.png')
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def collision(self, hero):
		if self.x < hero.x + hero.width and self.x + self.size > hero.x and self.y < hero.y + hero.height and self.y + self.size > hero.y:
			return True
		return False
			
	def move(self, vx):
		self.x += vx
		
	def show(self, surface):
		surface.blit(self.image, (self.x, self.y))
			