from config import *
import random

class snake():
    UP='up'
    DOWN='down'
    LEFT='left'
    RIGHT='right'
    HEAD=0

    def __init__(self):
        self.x= random.randint(4,config.CELLWIDTH -6)
        self.y= random.randint(4,config.CELLHEIGHT -6)
        self.direction = self.RIGHT
        self.snakeCoords=[{'x':self.x, 'y': self.y},
                        {'x':self.x-1, 'y': self.y},
                        {'x':self.x-2, 'y': self.y}]
    def update(self,apple):
        if self.snakeCoords[self.HEAD]['x'] == apple.x and self.snakeCoords[self.HEAD]['y'] == apple.y:
            apple.setNewLocation()
        else:
            del self.snakeCoords[-1]

        if self.direction == self.DOWN:
            newHead ={'x': self.snakeCoords[self.HEAD]['x'],'y': self.snakeCoords[self.HEAD]['y']+1}
        elif self.direction == self.UP:
            newHead ={'x': self.snakeCoords[self.HEAD]['x'],'y': self.snakeCoords[self.HEAD]['y']-1}
        elif self.direction == self.LEFT:
            newHead ={'x': self.snakeCoords[self.HEAD]['x']-1,'y': self.snakeCoords[self.HEAD]['y']}
        elif self.direction == self.RIGHT:
            newHead ={'x': self.snakeCoords[self.HEAD]['x']+1,'y': self.snakeCoords[self.HEAD]['y']}

        self.snakeCoords.insert(0, newHead)