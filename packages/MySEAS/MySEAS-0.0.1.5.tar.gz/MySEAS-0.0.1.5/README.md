# Introduction
NOTE: This is under development and does not have many features.

This is a python Framework called MySEAS (My Sufficiently exploited and Affordable Script). Its build on top of pygame, thefore the name. In the future you might be able to call it a game engine but right now Its a tool i guess.
It (by the moment) does not have a UI and not many features. Of course u can excpect a lot of features in the future.

Anyway here is a code example of how u can use this.

## MAIN FILE:
    
    from SEAS import *
    from moveCar import *
    from moveCar2 import *

    SEAS.loggingLevel = 'Warning'

    SEAS.newScene('S1', 60, True)
    SEAS.newScene('S2', 60, False)


    # Object components
    carCords = [[10, 10], [10, 20], [30, 20], [30, 10]]
    carComps = [TransformPoly(carCords), RenderPoly(), CharacterPolyController(), CarMovement(), HitboxPoly(), CollidePoly()]

    testCords = [[200, 200], [300, 200], [300, 300], [200, 300]]
    testComps = [TransformPoly(testCords), RenderPoly(), HitboxPoly(), CarMovement2(), CharacterPolyController(), CollidePoly()]

    # Create objects
    SEAS.getScene().addObject(objectName='Car', components=carComps)
    SEAS.getScene().addObject(objectName='Test', components=testComps)

    # Object hitboxes
    SEAS.createHitboxGroup('Finish', True)
    SEAS.addNameHitboxGroup('Finish', ['Car', 'Test'])

    # Create Materials
    SEAS.createMaterial(materialName='Car', materialColor='#d65d0e')
    SEAS.createMaterial(materialName='Test', materialColor='#ffffff')

    # Adding Materials
    SEAS.addMaterial(materialName='Car', objectName='Car')
    SEAS.addMaterial(materialName='Test', objectName='Test')


    SEAS.coreModules['Screen'].color = "#282828"


    run()


## carMovement1 FILE:

    from SEAS import *


    class CarMovement:
        def start(self):
            self.cntrl = SEAS.getScene().getComponent('CharacterPolyController')
            self.trns = SEAS.getScene().getComponent('TransformPoly')
            self.coll = SEAS.getScene().getComponent('CollidePoly')
            
            self.steerVel = 0.0 
            self.maxSteerVel = 4
            self.steerAcc = 1
            self.steerB = None

            self.gear = 1
            self.vel = 0.0
            self.drift = None
            self.acc = 10
            self.maxVel = 999 
            self.maxVelBack = 5

        def update(self):
            # VEL HANDLELING
            self.gearHandleling()
            self.steerHandleling()
            self.velHandleling()
            self.driftHandleling()
            self.moveCar()
            self.newMap()
            self.toggleHitbox()
        
        def toggleHitbox(self):
            if SEAS.input('SPACE') and SEAS.getHitboxGroupState('Finish'):
                SEAS.toggleHitboxGroup('Finish')


        def velHandleling(self): 
            if SEAS.input('w') and self.vel < self.maxVel: self.vel += self.acc
            if SEAS.input('s') and self.vel > -self.maxVelBack: self.vel -= self.acc

            if not SEAS.input('w') and self.gear == 1:
                self.vel -= self.acc
                if self.vel < 0: self.vel = 0

            if not SEAS.input('s') and self.gear == -1:
                self.vel += self.acc
                if self.vel > 0: self.vel = 0
        
        def steerHandleling(self):
            if SEAS.input('a') and self.steerVel > -self.maxSteerVel: self.steerVel -= self.steerAcc;
            if SEAS.input('d') and self.steerVel < self.maxSteerVel: self.steerVel += self.steerAcc; 

            if not SEAS.input('a') and self.steerVel < 0: self.steerVel += self.steerAcc; self.steerVel = 0 if self.steerVel > 0 else self.steerVel
            if not SEAS.input('d') and self.steerVel > 0: self.steerVel -= self.steerAcc; self.steerVel = 0 if self.steerVel < 0 else self.steerVel

            if SEAS.input('a') and SEAS.input('d'): self.steerVel = 0

        def driftHandleling(self):
            pass

        def gearHandleling(self):
            if self.vel > 0:  self.gear = 1
            if self.vel == 0: self.gear = 0
            if self.vel < 0: self.gear = -1

        def moveCar(self):
            self.cntrl.move(self.trns.angle, self.vel * SEAS.deltaTime)
            self.cntrl.rotate(self.steerVel)
            self.cntrl.drawDir()

        def newMap(self):
            if self.coll.collide:
                SEAS.transferObject('Car', 'S2', resetObject=False)
                SEAS.targetScene('S2')

## Carmovement2 FILE:
    from SEAS import *
    from moveCar import CarMovement


    class CarMovement2(CarMovement):
        def velHandleling(self):
            if SEAS.input('i') and self.vel < self.maxVel: self.vel += self.acc
            if SEAS.input('k') and self.vel > -self.maxVelBack: self.vel -= self.acc

            if not SEAS.input('i') and self.gear == 1:
                self.vel -= self.acc
                if self.vel < 0: self.vel = 0

            if not SEAS.input('k') and self.gear == -1:
                self.vel += self.acc
                if self.vel > 0: self.vel = 0

        def steerHandleling(self):
            if SEAS.input('j') and self.steerVel > -self.maxSteerVel: self.steerVel -= self.steerAcc;
            if SEAS.input('l') and self.steerVel < self.maxSteerVel: self.steerVel += self.steerAcc; 

            if not SEAS.input('j') and self.steerVel < 0: self.steerVel += self.steerAcc; self.steerVel = 0 if self.steerVel > 0 else self.steerVel
            if not SEAS.input('l') and self.steerVel > 0: self.steerVel -= self.steerAcc; self.steerVel = 0 if self.steerVel < 0 else self.steerVel

            if SEAS.input('j') and SEAS.input('l'): self.steerVel = 0


Its a suprise what this does
This code does not display all of the current features but this is a very simple example and u can go a lot longer.

# Explaining the code (and more)
Too understand whats going on u can do two things. Use ur brain and see what the functions do or look at the documentation.md.

# Download
The procces to download this is quit simple. Just use pip.
Pip command:
pip install MySEAS (If u know what ur doing u can ofc use pip3)

U can also visit the page on pypi here:
https://pypi.org/project/MySEAS/


# Patron
u thought
