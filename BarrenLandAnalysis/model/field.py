from shapely.geometry import box, Polygon


class Field:
    """
    Represents a field using a shapely polygon.
    """

    def __init__(self, len, width):
        self._fieldPolygon = box(0, 0, len, width)

    def area(self):
        """
        Returns a list representing the area of the feild. If the feild has
        been seperated into two sperate areas the list will have a size of 2
        """
        if isinstance(self._fieldPolygon, Polygon):
            return [self._fieldPolygon.area]

        fieldAreas = []
        for field in self._fieldPolygon:
            fieldAreas.append(field.area)

        fieldAreas.sort()
        return fieldAreas

    def removeBarrenArea(self, barrenField):
        """
        Removes a part of the feild that is not to be included in the field
        """
        self._fieldPolygon = self._fieldPolygon.difference(barrenField)
