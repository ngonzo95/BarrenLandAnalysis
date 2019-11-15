from BarrenLandAnalysis.model.field import Field
from BarrenLandAnalysis.service.parseInput import parseBarrenFieldInput
from BarrenLandAnalysis.exception.fieldParsingException import (
    FieldParsingException)


def main():
    """
    Takes in user specified barren land and outputs the area of the reamining
    Land
    """
    # Initalize a new feild with new barren spots
    field = Field(400, 600)

    try:
        # Convert the input into a list of rectangles
        strInput = input("Please input the barren field set: ")
        while '}' not in strInput:
            strInput += input(":")

        barrenFields = parseBarrenFieldInput(strInput)
    except FieldParsingException as e:
        # If there is a parsing error alert the user and exit
        print(str(e))
        return

    # Subract all of the barren feilds from the field
    for barrenField in barrenFields:
        field.removeBarrenArea(barrenField.createContinuosBox())

    # Calculate the area from the remaining feild
    areaList = field.area()

    # Print out the area list in the desired format
    outputString = ""
    for area in areaList:
        outputString += str(int(area)) + " "

    print(outputString.strip())


if __name__ == '__main__':
    main()
