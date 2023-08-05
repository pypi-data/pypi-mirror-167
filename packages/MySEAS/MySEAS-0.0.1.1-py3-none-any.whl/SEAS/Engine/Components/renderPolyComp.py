from SEAS.Engine.Setup import *
from SEAS.Engine.Core import *


class RenderPoly:
    def start(self):
        self.transformComp = SEAS.getScene().getComponent('TransformPoly')

    def update(self):
        try:
            objectColor = SEAS.getMaterial()
            points = self.transformComp.points
            pygame.draw.polygon(SEAS.coreModules['Screen'].wn, objectColor, points)
        except:
            if SEAS.loggingLevel == 'Warning' or SEAS.loggingLevel == 'Comment':
                print('RENDERPOLY: WARNING: Scene has no objects (yet)\nTo disable this text showing up make SEAS.loggingLevel=Error')
