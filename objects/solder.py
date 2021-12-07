'''Файл содержит объекты игрока и противников'''

import pygame as pg
from objects.map import Object
import sys
import datetime

'''Основной класс для игрока и противников'''
class Solder(Object):
	def __init__(self, screen, X, Y, color):
		super().__init__(screen, X, Y)
		self.image = pg.Rect((0,0,self.cellSize, self.cellSize))
		self.color = color
		
	def draw(self):
		self.screen_rect = self.screen.get_rect()
		pg.draw.rect(self.screen, self.color , self.image)

'''Класс игрока'''		
class Player(Solder):
	def __init__(self, screen):
		super().__init__(screen, 0, 0, 'BLUE')
		self.image.centerx = self.screen_rect.centerx
		self.image.centery = self.screen_rect.centery
		self.point = False
		self.speed = 1
		self.clicktime = False #счетчик времени от нажатя до отпускания кнопки мыши
	
	#назначаем точку для движения	
	def start_moving(self, pos, map):
		self.point =[round((pos[0] - map.X) / self.cellSize) * self.cellSize + self.cellSize/2, round((pos[0] - map.Y) / self.cellSize) * self.cellSize + self.cellSize/2]
		
		#self.point = [pos_cor[0], pos_cor[1]]
	
	#рисуем линию движения		
	def drow_moving_line(self):
		if self.point:
			pg.draw.line(self.screen, 'YELLOW', self.image.center, self.point)	
			
	def moving(self):
		if self.point:
			if self.image.center != self.point:
				if self.image.centerx > self.point[0]:
					self.X -= self.speed
					self.point[0] += self.speed
				elif self.image.centerx < self.point[0]:
					self.X += self.speed
					self.point[0] -= self.speed
					
				if self.image.centery > self.point[1]:
					self.Y -= self.speed
					self.point[1] += self.speed
				elif self.image.centery < self.point[1]:
					self.Y += self.speed
					self.point[1] -= self.speed
				
	def events(self, map):
		for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.exit()
				if  event.type == pg.MOUSEBUTTONDOWN:
					self.clicktime = datetime.datetime.now().timestamp()
				if event.type == pg.MOUSEBUTTONUP:
					self.clicktime = datetime.datetime.now().timestamp() - self.clicktime
					if self.clicktime:
						if self.clicktime < 0.5 :
							self.start_moving(event.pos, map)
						else:
							print(self.clicktime)
						return False	
				
						
			
		