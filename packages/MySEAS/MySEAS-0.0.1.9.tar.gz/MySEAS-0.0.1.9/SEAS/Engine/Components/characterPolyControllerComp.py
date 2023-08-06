from SEAS.Engine.Core import *
from SEAS.Engine.Setup import *

import math


class CharacterPolyController:
    def start(self): 
        self.trns = SEAS.getScene().getComponent('TransformPoly')
        self.hitb = SEAS.getScene().getComponent('HitboxPoly')

    def update(self): 
        pass

    
    def move(self, angle, vel):
        mX = math.cos(math.radians(angle)) * vel
        mY = math.sin(math.radians(angle)) * vel

        self.moveX(mX)
        self.moveY(mY)


    # make so that points move in the future
    def rotate(self, angle):
        self.trns.angle += angle

    def drawDir(self):
        len = 50
        lenK1 = math.cos(math.radians(self.trns.angle))*len
        lenK2 = math.sin(math.radians(self.trns.angle))*len

        
        pygame.draw.line(SEAS.coreModules['Screen'].wn,
                (0, 255, 0), 
                (self.trns.points[0][0], self.trns.points[0][1]), 
                (lenK1+self.trns.points[0][0], lenK2+self.trns.points[0][1]) )

    def moveX(self, vel):
        for point in self.trns.points:
            point[0] += vel

    def moveY(self, vel):
        for point in self.trns.points:
            point[1] += vel
