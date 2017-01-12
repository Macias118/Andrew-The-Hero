import pygame
from Colors import *

class Brick():
	
	def __init__(self, x, y, s, c):
		self.x = x
		self.y = y
		self.size = s
		self.color = c
		self.rect = [self.x, self.y, self.size, self.size]
		
	def show(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)