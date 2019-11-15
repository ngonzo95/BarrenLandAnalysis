from shapely.geometry import box, Polygon


class Field:
    def __init__(self, len, width):
        self._fieldPolygon = box(0, 0, len, width)

    def area(self):
        if isinstance(self._fieldPolygon, Polygon):
            return [self._fieldPolygon.area]

        fieldAreas = []
        for field in self._fieldPolygon:
            fieldAreas.append(field.area)

        fieldAreas.sort()
        return fieldAreas

    def removeBarrenArea(self, barrenField):
        self._fieldPolygon = self._fieldPolygon.difference(barrenField)
