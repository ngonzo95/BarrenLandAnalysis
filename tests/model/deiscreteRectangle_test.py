from BarrenLandAnalysis.model.discreteRectangle import DiscreteRectangle
from shapely.geometry import box


def test_modelEquality():
    assert DiscreteRectangle(
        0, 0, 100, 100) == DiscreteRectangle(0, 0, 100, 100)

    assert not DiscreteRectangle(
        0, 0, 10, 10) == DiscreteRectangle(1, 1, 10, 10)


def test_createContinuosBox():
    fieldInDiscreteSpace = DiscreteRectangle(0, 0, 9, 9)
    fieldInContinuosSpace = box(0, 0, 10, 10)
    assert fieldInDiscreteSpace.createContinuosBox() == fieldInContinuosSpace
