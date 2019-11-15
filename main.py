from BarrenLandAnalysis.model.field import Field
from BarrenLandAnalysis.service.parseInput import parseBarrenFieldInput


def main():
    field = Field(400, 600)
    strInput = input()

    barrenFields = parseBarrenFieldInput(strInput)

    for barrenField in barrenFields:
        field.removeBarrenArea(barrenField.createContinuosBox())

    areaList = field.area()

    outputString = ""

    for area in areaList:
        outputString += str(int(area)) + " "

    print(outputString.strip())


if __name__ == '__main__':
    main()
