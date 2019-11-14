class DiscreteRectangle:
    def __init__(self, x1, y1, x2, y2):
        self.startCorner = (x1, y1)
        self.endCorner = (x2, y2)

    def __eq__(self, obj):
        return (self.startCorner == obj.startCorner
                and self.endCorner == obj.endCorner)

    def __str__(self):
        return ("StartCorner: " + str(self.startCorner) + " EndCorner: "
                + str(self.endCorner))
