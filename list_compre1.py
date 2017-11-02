# printing the cubes of numbers through 1 to 10 using list comprehension

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four