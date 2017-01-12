import pygame

class Andrew():
		
	x = 210
	y = 400
	width = 46
	height = 82
	hp = 100
	
	image = pygame.image.load('andrew.png')
	imageLeft = pygame.image.load('andrewLeft.png')
	imageDown = pygame.image.load('andrewDown.png')
	imageDownLeft = pygame.image.load('andrewDownLeft.png')
	canJump = False
	timeToShoot = 0
	
	def set_timeToShoot(self, value):
		self.timeToShoot = value
		
	def make_crosshair(self):
		size = 6
		xm = pygame.mouse.get_pos()[0]
		ym = pygame.mouse.get_pos()[1]
		
		# drawing crosshair
		a = xm - size						# 1   2
		b = xm + size						#  \ /
		c = ym - size						#   0
		d = ym + size						#  / \
											# 4   3
			
		p0 = (xm,ym)
		p1 = (a,c)
		p2 = (b,c)
		p3 = (b,d)
		p4 = (a,d)
		
		points = [ p1, p0, p2, p0, p3, p0, p4, p0, p1 ]
		return points
		
	def move(self, dx):
		self.x += dx
		
	def jump(self, v0):
		self.y -= v0
		
	def show(self, surface):
		if pygame.mouse.get_pos()[0] < self.x:
			if pygame.key.get_pressed()[pygame.K_s]:
				surface.blit(self.imageDownLeft, (self.x, self.y+50))
				self.canJump = False
			else:
				surface.blit(self.imageLeft, (self.x, self.y))
		elif pygame.mouse.get_pos()[0] > self.x:
			if pygame.key.get_pressed()[pygame.K_s]:
				surface.blit(self.imageDown, (self.x-35, self.y+50))
				self.canJump = False
			else:
				surface.blit(self.image, (self.x, self.y))
	'''		
	def collision(self, brickList):
		for brick in brickList:
			if self.x + self.width > brick.x and self.x < brick.x + brick.size:
				if self.y + self.height <= brick.y + brick.size:
					return brick
		return False
	'''
	def collision(self, enemyList):
		for enemy in enemyList:
			if self.x + self.width > enemy.x and self.x < enemy.x + enemy.width and self.y + self.height > enemy.y and self.y < enemy.y + enemy.height:
				return True
		return False
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			