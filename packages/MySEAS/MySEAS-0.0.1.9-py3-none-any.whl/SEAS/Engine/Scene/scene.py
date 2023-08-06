from SEAS.Engine.Setup import *
from SEAS.Engine.Models.emptyModel import * 
from SEAS.Engine.Core.event import *
from SEAS.Engine.Core.screen import *

from typing import Any

import time

class Scene:
    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def __init__(self, frameLimit):
        self.clock = pygame.time.Clock()
        self.frameLimit = frameLimit
        self.framerate = 0
        self.objects = {}

    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def startObjects(self):
        for component in self.objects:
            self.currentObj = self.objects[component]
            self.objects[component].start()


    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def updateScene(self):

        # Updating objects, thats really just updating the blueprint that then updates the components of the object
        try:
            for object in self.objects:
                self.currentObj = self.objects[object]
                self.objects[object].update() 
        except RuntimeError:
            # This just basicly means that if a object was created in the dic we are gonna start OVEERERRERERERERER
            pass

        self.clock.tick(60)


    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def addObject(self, objectName:str="emptyModel", hitbox:bool=True, objectModel:Any=EmptyModel, components:list=[], objectLocation:str='objects') -> None: # Dont use objLocation, hitbox will later be hitbox groups and i t will be in the transform group
        # First get the location by getting the of my self
        location = getattr(self, objectLocation)

        # Then adding it to the attribute
        location[objectName] = objectModel()

        # Then adding the components we might want to add when we create the object
        self.objects[objectName].addComponent(components)

        # Adding a default white material
        self.objects[objectName].material = "#ffffff"

    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def getComponent(self, attribute=''):
        # If nothing is specified return the object u r using
        if attribute == '':
            return self.currentObj
        

        # If it doesnt have the attribute just return the AttributeError 
        try:
            returnValue = self.currentObj.components[attribute]

            return returnValue  

        except AttributeError as err:
            raise err

    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def getRawComponent(self, object:str, attribute:str=''):
        # So were basicly doing getAttribute function but we specify the object and do not use the currentObj
        if attribute == '':
            return self.objects[object]


        try:
            returnValue = self.objects[object].components[attribute]

            return returnValue

        except AttributeError as err:
            raise err


    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def getObject(self):
        return self.currentObj

    def getRawObject(self, object:str):
        return self.objects[object]
    
    def getAllObject(self): # Will not return the obejct your calling from
        returnValue = []
        for obj in self.objects:
            if self.objects[obj] != self.currentObj:
                returnValue.append(self.objects[obj])

        return returnValue
    
    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def getAttribute(self, attribute):
        # Get the requested attribute of the current object

        try:
            returnValue = getattr(self.currentObj, attribute)
            return returnValue
        
        except AttributeError as err:
            raise err


    #-----------------------------------------------------------------------FUNC--------------------------------------------------------------
    def getRawAttribute(self, object, attribute):
        # Get the requested attribute of the object requested

        try:
            returnValue = getattr(self.objects[object], attribute)
            return returnValue

        except AttributeError as err:
            raise err
