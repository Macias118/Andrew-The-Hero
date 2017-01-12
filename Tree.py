import pygame

class Tree():
	
	image = pygame.image.load('tree.png')
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def move(self, vx):
		self.x += vx
		
	def show(self, surface):
		surface.blit(self.image, (self.x, self.y))