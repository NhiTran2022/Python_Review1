
'''
Imagine that there are cube boxes. (equal sides) and they are stacked in such a
way that the cube box contains a cube box that is just a size lesser than that
again the second box inside contains a lesser sized box and so on
until 1 x 1 x 1 sixed cube box
For example cube box with 5 inch each side (5 x 5 x 5)
has a cube box 4 x 4 x 4,
has a cube box 3 x 3 x 3,
has a cube box 2 x 2 x 2,
has a cube box 1 x 1 x 1
The problem is to find the total volume of all the boxes
'''
def volumeOfBox(sides):
    if sides == 1:
        return 1
    else:
        print("Calculating volume for the box of side ", sides)
        vol = sides * sides * sides
        print("Volume fo this box is ", vol)
        return vol + volumeOfBox(sides-1)
x = int(input("Enter the measurement of the largest box you have : "))
print("The total Volume of all the boxes : ", volumeOfBox(x))
