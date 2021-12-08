'''Файл содержит объект карты, ячеек и всех статических оъектов'''
import pygame as pg

'''Основной объект.От него наследуются все объекты игры'''


class Object():
    def __init__(self, screen, X, Y):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.X = X
        self.Y = Y
        self.cellSize = 20  # размер клетки


'''Класс карты'''


class Map(Object):
    def __init__(self, screen):
        super().__init__(screen, 0, 0)
        self.color = 'GREEN'
        # определяем размеры поля
        self.mapSize = (100, 100)  # размер карты в клетках
        self.mapSizePx = [i * self.cellSize for i in self.mapSize]  # размер карты в пикселях
        self.image = pg.Rect((self.X, self.Y, self.mapSizePx[0], self.mapSizePx[1]))
        self.screen_rect = self.screen.get_rect()

    def draw(self, player):

        self.image.x = self.screen_rect.w / 2 - player.X - self.cellSize / 2
        self.image.y = self.screen_rect.h / 2 - player.Y - self.cellSize / 2
        pg.draw.rect(self.screen, self.color, self.image)

        # Рисуем сетку
        # Вертикальные линии
        for cell in range(self.mapSize[0]):
            pg.draw.line(self.screen, 'WHITE', [self.image.x + cell * self.cellSize, self.image.y],
                         [self.image.x + cell * self.cellSize, self.image.y + self.mapSizePx[1]])
        # Горзонтальные линии
        for cell in range(self.mapSize[1]):
            pg.draw.line(self.screen, 'WHITE', [self.image.x, self.image.y + cell * self.cellSize],
                         [self.image.x + self.mapSizePx[0], self.image.y + cell * self.cellSize])


'''класс ячкйки'''


class cell(object):
    def __init__(self, screen, X, Y, cross, level):
        super().__init__(screen, X, Y)
        self.cross = cross  # возможность перксечения
        self.level = level  # уровень повкрхности
