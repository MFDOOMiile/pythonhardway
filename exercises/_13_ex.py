from sys import argv
# read the WYSS section for how to run this
# script, first, second, third = argv

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)


# script, first, second = argv #script with one less argument

# print("The script is called:", script)
# print("Your first variable goes here:", first)
# print("Your second variable goes here", second)

script, bee, lion, dog, sloth = argv #script with one more argument

print("The script is called:", script)
print("The first variable goes here:", bee)
print("The second variable goes here:", lion)
print("The third variable goes here:", dog)
print("The fourth variable goes here:", sloth)
