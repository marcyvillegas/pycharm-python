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

# Example 1
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

# Example 2
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]

print(codes)

codes_again = []

def orderCodes():
    for symbol in symbols:
        codes_again.append(ord(symbol))

    return codes_again

print(orderCodes())

# -- ARGS and KWARGS --

# >> Args
# allows us to pass a variable number of non-keyword arguments to a function
# Non-keyword here means that the arguments should not be a dictionary (key-value pair), and they can be numbers or strings.

def multiplyNumbers(*numbers):
    product = 1
    for n in numbers:
        product *= n
    return product


print("product:", multiplyNumbers(4, 4, 4, 4, 4, 4))

# >> Kwargs
# allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result

print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))

