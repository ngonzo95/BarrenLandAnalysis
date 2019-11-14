from shapely.geometry import box

outterBox = box(0, 0, 400, 600)
innerBox = box( 0, 292, 400, 308)

output = outterBox.difference(innerBox)

print(output)
print("Area: " + str(output.area))

for p in output:
    print("feild: " + str(p))
    print("Area: " + str(p.area))
