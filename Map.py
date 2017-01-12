import pygame
import random
from Colors import *
from Andrew import *
from Bullet import *
from Brick import *

class Map():
	x = 0
	y = 0
	width = 10000
	height = 800
	image = pygame.image.load('map.bmp')  
	
	def __init__(self):
		pass
		
	def show(self, surface):
		surface.blit(self.image, (self.x, self.y))
	
	def move(self, vx):
		self.x += vx