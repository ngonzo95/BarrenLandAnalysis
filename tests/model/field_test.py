from BarrenLandAnalysis.model.field import Field
from shapely.geometry import box


def test_fieldHasFullAreaWhenItHasNoBarrenLand():
    field = Field(100, 100)
    assert field.area() == [10000]


def test_fieldWithBarrenLandInTheCenterSubtractsBarrenLandFromArea():
    field = Field(100, 100)
    field.removeBarrenArea(box(10, 10, 20, 20))
    assert field.area() == [10000 - 100]


def test_fieldWithBarrenLandDividingFieldReturnsTwoFieldAreas():
    field = Field(100, 100)
    field.removeBarrenArea(box(45, 0, 55, 100))
    assert field.area() == [4500, 4500]


def test_fieldWithMultipleSpotsOfBarrenLandReturnsOneArea():
    field = Field(100, 100)
    field.removeBarrenArea(box(10, 10, 20, 20))
    field.removeBarrenArea(box(30, 30, 40, 40))
    assert field.area() == [10000 - 100 - 100]


def test_fieldWithMultipleSpotsOfBarrenLandNextToEachOther():
    field = Field(100, 100)
    field.removeBarrenArea(box(10, 10, 20, 20))
    field.removeBarrenArea(box(10, 20, 20, 30))
    assert field.area() == [10000 - 100 - 100]


def test_fieldWithMultipleSpotsOfBarrenLandThatShareOnePoint():
    field = Field(100, 100)
    field.removeBarrenArea(box(10, 10, 20, 20))
    field.removeBarrenArea(box(20, 20, 30, 30))
    assert field.area() == [10000 - 100 - 100]


def test_fieldWithMultipleAreasSortedCorrectly():
    field = Field(100, 100)
    field.removeBarrenArea(box(20, 0, 30, 100))
    field.removeBarrenArea(box(60, 0, 65, 100))
    assert field.area() == [20 * 100, 30 * 100, 35 * 100]


def test_fieldWithAreaSplitIntoSixSectorsWorks():
    field = Field(100, 100)
    field.removeBarrenArea(box(30, 0, 40, 100))
    field.removeBarrenArea(box(60, 0, 90, 100))
    field.removeBarrenArea(box(0, 50, 100, 70))

    expectedAreas = [30 * 50, 20 * 50, 10 * 50, 30 * 30, 20 * 30, 10 * 30]
    expectedAreas.sort()

    assert field.area() == expectedAreas


def test_fieldWithMultipleOnePointConnectionsDividingField():
    field = Field(100, 100)
    field.removeBarrenArea(box(30, 0, 40, 30))
    field.removeBarrenArea(box(40, 30, 50, 80))
    field.removeBarrenArea(box(50, 80, 60, 100))

    expectedAreas = [30*30 + 40*50 + 50*20, 60*30 + 50*50 + 40*20]
    expectedAreas.sort()

    assert field.area() == expectedAreas
