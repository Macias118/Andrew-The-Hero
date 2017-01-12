import pygame
from Colors import *

class Bullet():

	color = orange
	size = 6
	velocity = 35

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.destX = pygame.mouse.get_pos()[0]
		self.destY = pygame.mouse.get_pos()[1]
		self.shoot()
		
	def shoot(self):
		distance = ( (self.destX - self.x) ** 2 + (self.destY - self.y) ** 2) ** (0.5)
		speed = distance / self.velocity
		
		try:
			self.dx = (self.destX - self.x) / speed
			self.dy = (self.destY - self.y) / speed
		except ZeroDivisionError:
			self.dx, self.dy = 0,0
			
	def move(self):
		self.x += self.dx
		self.y += self.dy
		
	def show(self, surface):
		pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)
		
	def collision(self, enemy):
		if ( self.x + self.size > enemy.x and self.x - self.size < enemy.x + enemy.width ) and ( self.y + self.size > enemy.y and self.y - self.size < enemy.y + enemy.height ):
			enemy.hp -= 20
			return True
		return False
	
		
		