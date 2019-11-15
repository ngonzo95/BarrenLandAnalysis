from BarrenLandAnalysis.model.discreteRectangle import DiscreteRectangle
from BarrenLandAnalysis.exception.fieldParsingException import (
    FieldParsingException)
import re

_RECTANGLE_SET_REGEX = "^{\\s*(?:\"[^\"]+\"\\s*,?\\s*)*}$"
_RECTANGLE_EXTRACTION_REGEX = "\"[^\"]+\"(?=\\s*(?=,|}))"
_COORD_EXTRACTION_REGEX = "^\"(\\d+) (\\d+) (\\d+) (\\d+)\"$"


def parseBarrenFieldInput(inputString):
    _validateInputString(inputString)
    matches = re.findall(_RECTANGLE_EXTRACTION_REGEX, inputString)

    rectangles = []
    for idx, fieldStr in enumerate(matches):
        coords = _getCoords(fieldStr, idx)

        r = DiscreteRectangle(int(coords[0]), int(coords[1]),
                              int(coords[2]), int(coords[3]))
        rectangles.append(r)
    return rectangles


def _validateInputString(inputString):
    if not (inputString.startswith("{") and inputString.endswith("}")):
        raise FieldParsingException("Missing curly brace in input")

    if not re.fullmatch(_RECTANGLE_SET_REGEX, inputString):
        raise FieldParsingException("Rectangle set is improperly formatted")


def _getCoords(fieldStr, rectanglePos):
    coords = re.fullmatch(_COORD_EXTRACTION_REGEX, fieldStr)
    if not coords:
        raise FieldParsingException("Rectangle at position "
                                    + str(rectanglePos) + " is misformatted")
    return coords.groups()
