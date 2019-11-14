from shapely.geometry import box


class DiscreteRectangle:
    def __init__(self, x1, y1, x2, y2):
        self._startCorner = (x1, y1)
        self._endCorner = (x2, y2)

    def __eq__(self, obj):
        return (self._startCorner == obj._startCorner
                and self._endCorner == obj._endCorner)

    def __str__(self):
        return ("StartCorner: " + str(self._startCorner) + " EndCorner: "
                + str(self._endCorner))

    def createContinuosBox(self):
        return box(self._startCorner[0],
                   self._startCorner[1],
                   self._endCorner[0] + 1,
                   self._endCorner[1] + 1)
