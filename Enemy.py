import pygame

class Enemy():
	
	width = 124
	height = 82
	def __init__(self, x, y, c):
		self.x = x
		self.y = y - self.height
		if c == 'blue':
			self.image = pygame.image.load('enemy_blue.png')
			self.hp = 75
		elif c == 'red':
			self.image = pygame.image.load('enemy_red.png')
			self.hp = 100
		elif c == 'green':
			self.image = pygame.image.load('enemy_green.png')
			self.hp = 50
		elif c == 'pink':
			self.image = pygame.image.load('enemy_pink.png')
			self.hp = 40
		else:
			self.image = pygame.image.load('enemy_white.png')
			self.hp = 20
			
	def move(self, vx):
		self.x -= vx
			
	def show(self, surface):
		surface.blit(self.image, (self.x, self.y))
		
		
					