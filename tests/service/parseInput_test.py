
import BarrenLandAnalysis.service.parseInput as serviceUnderTest
from BarrenLandAnalysis.model.discreteRectangle import DiscreteRectangle
from BarrenLandAnalysis.exception.fieldParsingException import (
    FieldParsingException)
import pytest


# TODO Ask more questions about input parsing and write tests accordingly
def test_ensureParserChecksForBracesAndWorksForNoInputs():
    assert serviceUnderTest.parseBarrenFieldInput("{}") == []

    with pytest.raises(FieldParsingException,
                       match="Missing curly brace in input"):
        serviceUnderTest.parseBarrenFieldInput("\"\"}")

    with pytest.raises(FieldParsingException,
                       match="Missing curly brace in input"):
        serviceUnderTest.parseBarrenFieldInput("{\"\"")


def test_oneBoxEntered_parsescorrectly():
    inputString = "{\"0 292 399 307\"}"

    expectedOutput = [DiscreteRectangle(0, 292, 399, 307)]
    assert (serviceUnderTest.parseBarrenFieldInput(inputString)
            == expectedOutput)


def test_multipleBoxesEntered_parsesCorrectly():
    inputString = "{\"0 292 399 307\", \"1 50 250 300\", \"80 80 80 80\"}"
    expectedOutput = [DiscreteRectangle(0, 292, 399, 307),
                      DiscreteRectangle(1, 50, 250, 300),
                      DiscreteRectangle(80, 80, 80, 80)]

    assert (serviceUnderTest.parseBarrenFieldInput(inputString)
            == expectedOutput)


def test_poorlySeperatedSetOfRectanglesRaisesAnException():
    with pytest.raises(FieldParsingException,
                       match="Rectangle set is improperly formatted"):
        serviceUnderTest.parseBarrenFieldInput(
            "{\"0 292 399 307\", blag\"1 50 250 300\", "
            + "\"80 80 80 80\"}")


def test_poorlyFormattedRectangleRaisesAndSaysWhichRectangle():
    with pytest.raises(FieldParsingException,
                       match="Rectangle at position 2 is misformatted"):
        serviceUnderTest.parseBarrenFieldInput(
            "{\"0 292 399 307\", \"1 50 250 300\", \"80 80 80 12 12\"}")


def test_inputWithVariousWhiteSpacesWorks():
    inputString = "{ \"0 292 399 307\",\"1 50 250 300\"\t,\n \"80 80 80 80\" }"
    expectedOutput = [DiscreteRectangle(0, 292, 399, 307),
                      DiscreteRectangle(1, 50, 250, 300),
                      DiscreteRectangle(80, 80, 80, 80)]
    assert (serviceUnderTest.parseBarrenFieldInput(inputString)
            == expectedOutput)
