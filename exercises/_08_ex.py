formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "Own tet here", 
    "Maybe a poem", 
    "or a song about fear"
))

# Mistakes Made:
#   Put " " for the True/False on line 5
#   Also put " " for the formatter on line 6