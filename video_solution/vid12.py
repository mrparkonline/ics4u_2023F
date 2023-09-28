''' Triangle Times Canadian Computing Competition: 2014 Stage 1, Junior #1
You have trouble remembering which type of triangle is which. You write a program to help.

Your program reads in three angles (in degrees).
    If all three angles are 60, output Equilateral.
    If the three angles add up to 180 and exactly two of the angles are the same, output Isosceles.
    If the three angles add up to 180 and no two angles are the same, output Scalene.
    If the three angles do not add up to 180, output Error.
'''

# input
angle1 = int(input("Enter angle 1:"))
angle2 = int(input("Enter angle 2:"))
angle3 = int(input("Enter angle 3:"))

# processing
angle_sum = angle1 + angle2 + angle3
# angle_sum = sum([angle1, angle2, angle3])

if angle_sum != 180:
    print("Error.")
else:
    # We can assume we have a valid triangle
    if angle1 == angle2 == angle3: # this is chaining the comparison operator of ==
        print("Equilateral")
    elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
        print("Scalene")
    else:
        print("Isosceles")