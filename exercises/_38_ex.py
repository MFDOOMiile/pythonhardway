###~~~Doing Things to Lists~~~###

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait! There are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Gril!", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do something with stuff!")

print(stuff[1])
print(stuff[-1]) #whoa! fancy fancy
print(stuff.pop())
print(' '.join(stuff)) #WHAT?!? COOL!!
print('#'.join(stuff[3:5]))  #SUPER DEDUPER STELLAR!