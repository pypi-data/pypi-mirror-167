class TransformPoly:
    def __init__(self, point):
        # Make so points are relavant to other points

        # We do this because the currentObj is not updated yet. This wont do a diff here but its good practise (look at hitboxPoly)
        self.inpPoint = point


    def start(self):
        self.points = self.inpPoint
        self.angle = 0

    def update(self):
        pass
