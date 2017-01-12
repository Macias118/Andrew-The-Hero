import pygame
import random
from Colors import *
from Andrew import *
from Bullet import *
from Brick import *
from Enemy import *
from Map import *
from Tree import *
from Coin import *

class Main():
	
	def __init__(self):
		self.height = 800
		self.width = 1200
		
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)# | pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.time = 30							# speed of the game
		pygame.mouse.set_visible(False)			# invisible cursor
		
		self.ground = 670
		
		self.bulletList = []
		self.brickList = []
		self.enemyList = []
		self.treeList = []
		
		self.background = Map()
		
		
		#self.make_bricks()
		self.make_trees()
		self.make_enemies()
		
		self.Hero = Andrew()
		self.accelerationOfGravity = 0.65
		self.coin = Coin(10000 - self.width / 2, self.ground - self.Hero.height)
	
	def make_bricks(self):
		height = 200
		for z in range(300, 1100, 30):
			height -= random.randint(-10, 10)
			brick = Brick(z, height, 20, red)
			self.brickList.append(brick)
			
		height = 400
		for z in range(300, 1100, 30):
			height -= random.randint(-10, 10)
			brick = Brick(z, height, 20, red)
			self.brickList.append(brick)
			
		height = 600
		for z in range(300, 1100, 30):
			height -= random.randint(-10, 10)
			brick = Brick(z, height, 20, red)
			self.brickList.append(brick)
	
	def make_enemies(self):
		for i in range(300, 12000, 100):
			self.enemyList.append(Enemy(self.width+i, self.ground, 'blue'))
		for i in range(3100, 12100, 300):
			self.enemyList.append(Enemy(self.width+i, self.ground, 'green'))
		for i in range(3500, 12150, 200):
			self.enemyList.append(Enemy(self.width+i, self.ground, 'pink'))
		for i in range(3750, 12300, 500):
			self.enemyList.append(Enemy(self.width+i, self.ground, 'red'))
		
	def make_trees(self):
		height = 400 - 50
		for i in range(0, 9850, 100):
			height += random.randint(-5, 5)
			self.treeList.append(Tree(i, height))
		
	def message(self, content, size, x, y, color):

		text = pygame.font.Font('freesansbold.ttf', size)
		textSurface = text.render(content, True, color)
		textRect = textSurface.get_rect()
		textRect.center = (x,y)
		self.screen.blit(textSurface, textRect)	

		
		
	def main(self):
		gameQuit = False
		nearly_end_game = False
		self.ground = 670
		land = self.ground
		v0 = 0
		vx = 18
		type_of_weapon = 15		# the higher the number, the worse the weapon
		attacked = 0
		end_x = 0
		end_y = 0
			
		while not gameQuit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameQuit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameQuit = True
						nearly_end_game = True
					if event.key == pygame.K_1:
						type_of_weapon = 15
					if event.key == pygame.K_2:
						type_of_weapon = 10
					if event.key == pygame.K_3:
						type_of_weapon = 7
					if event.key == pygame.K_4:
						type_of_weapon = 3
					if event.key == pygame.K_5:
						type_of_weapon = 1
					if event.key == pygame.K_q:
						vx = 50
					if event.key == pygame.K_r:
						self.Hero.x = 8000
					
							
						
			if pygame.mouse.get_pressed()[0] == 1:
				if attacked <= 0:
					if self.Hero.timeToShoot <= 0:		
						self.bulletList.append(Bullet(self.Hero.x+self.Hero.width/2, self.Hero.y+self.Hero.height/2))
						self.Hero.timeToShoot = type_of_weapon

			if pygame.key.get_pressed()[pygame.K_a]:
				if attacked <= 0:
					if self.Hero.x > 200:
						self.Hero.move((-1)*vx)	
					else:
						if self.background.x + vx < 0:
							self.background.move(vx)
							self.coin.move(vx)
							for tree in self.treeList:
								tree.move(vx)
							for enemy in self.enemyList:
								enemy.move((-1)*vx)	
			if pygame.key.get_pressed()[pygame.K_d]:
				if attacked <= 0:
					if self.Hero.x < 600:
						self.Hero.move(vx)	
					else:
						if self.background.x + self.background.width - vx > self.width:
							self.background.move((-1)*vx)
							self.coin.move((-1)*vx)
							for tree in self.treeList:
								tree.move((-1)*vx)
							for enemy in self.enemyList:
								enemy.move(vx)	
							if self.Hero.x < 200:
								self.Hero.move(vx)

			if pygame.key.get_pressed()[pygame.K_w]:
				if self.Hero.canJump == True:
					v0 = 12
					self.Hero.jump(v0)
					self.Hero.canJump = False
			
			# gravity
			if self.Hero.y + self.Hero.height < self.ground:
				v0 -= self.accelerationOfGravity
				self.Hero.jump(v0)
			else: # self.Hero.y >= self.ground:
				self.Hero.canJump = True
				v0 = 0
			if v0 < 0:
				self.Hero.canJump = False
			
			# collision with bricks
			'''
			if self.Hero.collision(self.brickList) != False:
				brick = self.Hero.collision(self.brickList)
				self.ground = brick.y
			else:
				self.ground = land				
			'''
			
			# collision hero with coin
			if self.coin.collision(self.Hero):
				gameQuit = True
				end_x, end_y = self.Hero.x, self.Hero.y
			
			# collision hero with enemy
			if self.Hero.collision(self.enemyList):
				attacked = 25
			
			# collision bullet with enemy
			if self.bulletList != []:
				for bullet in self.bulletList:
					for enemy in self.enemyList:
						if bullet.collision(enemy) == True:
							self.bulletList.remove(bullet)
							del bullet
							if enemy.hp <= 0:
								self.enemyList.remove(enemy)
							break

			# shooting
			if self.Hero.timeToShoot > 0:
				self.Hero.timeToShoot -= 1
			
			# moving everything
			for bullet in self.bulletList:
				bullet.move()
			for enemy in self.enemyList:
				enemy.move((0.2)*vx)

			if attacked > 0:
				attacked -= 1
				self.Hero.x -= attacked

			'''
			if self.Hero.x < 200:
				self.Hero.x += 6
				attacked = 0
				if self.background.x + vx < 0:
					self.background.move(2*vx)
					for tree in self.treeList:
						tree.move(2*vx)
					for enemy in self.enemyList:
						enemy.move((-2)*vx)	
			'''
				
			# drawing everything
			self.screen.fill(grass)
				# background
			self.background.show(self.screen)	
				# line
			#pygame.draw.line(self.screen, platinum, (0, land), (self.width, land), 40)	
				# everything
			for enemy in self.enemyList:
				enemy.show(self.screen)
			for bullet in self.bulletList:
				bullet.show(self.screen)
				# hero
			self.Hero.show(self.screen)
				# trees
			for tree in self.treeList:
				tree.show(self.screen)
				# coin
			self.coin.show(self.screen)
				# 
			
				
			pygame.draw.polygon(self.screen, red, self.Hero.make_crosshair(), 3)
			
			# update
			pygame.display.update()
			self.clock.tick(self.time)		
					
# -----------------------------------------------------------------------------------
		# ending the game out of main loop
	
		hero = Andrew()
		hero.x = end_x
		hero.y = end_y
		
		while not nearly_end_game:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					nearly_end_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						nearly_end_game = True
				self.screen.fill(gold)
				self.message('YOU WIN!!!!', 100, 600, 400, black)
				hero.show(self.screen)
			pygame.display.update()
			
		pygame.quit()
		quit()
		
		
		
if __name__ == '__main__':
	pygame.init()
	game = Main()
	game.main()