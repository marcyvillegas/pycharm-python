# -- LIST --
mylist = ["apple", "banana", "cherry"]

# -- TUPLES --
mytuple = ("apple", "banana", "cherry")

# -- DICTIONARIES --
wife = {'name': 'Rose', 'age': 33}

print(wife.get("none", "sample"))
print(wife.get("name"))

# -- SETS --
set_1 = {1, 2, 3}
# set_2 = set([1, 2, 3])

set_1.add(4)
print(set_1)

# -- COMPREHENSION --
# let us create lists out of other lists

main_list = [1, 2, 3, 56, 23, 12, 65, 76, 5, 9, 7]

big_list = []
small_list = []

def createNewLists():
    for item in main_list:
        if item > 10:
            big_list.append(item)
        else:
            small_list.append(item)


createNewLists()
print(big_list)
print(small_list)


n = [(a, b) for a in range(1, 3) for b in range(1, 3)]
print(n)
# output: [(1, 1), (1, 2), (2, 1), (2, 2)]
# inner and outer loop

new_list = []
def listComprehension():
    for a in range(1, 3):
        for b in range(1, 3):
            new_list.append((a, b))

    return new_list

print(listComprehension())