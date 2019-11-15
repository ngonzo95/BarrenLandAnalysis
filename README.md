# BarrenLandAnalysis
## Introduction
This project was written as a part of a code
challenge. The goal of this project is to return
the area of farmable land in the field. The field
starts out entirely farmable but areas of barren
land can be input by the user. If the areas of
barren land entirely separate the field, two
subfields are created and their areas will be
returned separately.

## Running the Application
### Installation
This project was written in python using a
 virtualenv. To use the virtualenv clone the
 application, go into the project and run `. virtualenv/bin/activate`. If you are running in
a windows environment run `virtualenv/bin/activate.bat`. to exit from the virtualenv run `deactivate`.

### Starting the App
to start the app run main.py using `python
main.py`. Once the application starts it will
prompt you to input the set barren fields. The
project was designed to handle farms of arbitrary
sizes but main.py is run using a farm that is
400 by 600 as specified in the coding challenge.

### Inputing Barren Fields
Inputing barren fields follow a strict format.
barren fields are represented as rectangles. To
create these rectangles specify the lower left
and upper right corner. An example string would
be "10 10 20 20". It is important that these
numbers are separated by exactly one space. When
inputing the set start with a '{' and end with a
'}'. Rectangles are comma separated and white
space does not matter. Here is an
example input:
```
{ "0 9 399 20", "50 0 59 599"}
```
The output for this would be:
```
450 3060 28950 196860
```
When the output has multiple fields the area of
those fields will be sorted from smallest to
largest.

## Running Tests
This project has a test suite that was written
with pytest. To run the test suite you must
be in the virtualenv. Then you can run `pytest`
in the root directory.

## Design Decisions
This project was built using sympy's
shapely.geomety package. I chose to use this
package because it already had efficient
operations for removing parts of a shape. The
major difficulty with working with this package
was transforming inputs from discrete to
continuous space. The basic solution to this was
to add 1 to the max points of the rectangles. For
parsing string input I used the re package. This
package is well tested and makes updating parsing
rules easy.
