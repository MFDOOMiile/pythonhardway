###~~~Strings & Text~~~###

types_of_people = 10 #setting a value of 10 to types_of_people
x = f"There are {types_of_people} types of people." #formatting a string and giving the string a value of x

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)