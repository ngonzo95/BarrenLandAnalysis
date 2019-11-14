from BarrenLandAnalysis.model.discreteRectangle import DiscreteRectangle
from BarrenLandAnalysis.exception.fieldParsingException import (
    FieldParsingException)


def parseBarrenFieldInput(inputString):

    if not (inputString.startswith("{") and inputString.endswith("}")):
        raise FieldParsingException("Missing curly brace in input")

    inputString = inputString.strip("{")
    inputString = inputString.strip("}")
    rectangles = []

    if inputString == "":
        return []

    for fieldStr in inputString.split(", "):
        fieldStr = fieldStr.strip("\"")
        print(fieldStr)
        coords = fieldStr.split(" ")
        r = DiscreteRectangle(int(coords[0]), int(coords[1]),
                              int(coords[2]), int(coords[3]))
        rectangles.append(r)

    return rectangles
