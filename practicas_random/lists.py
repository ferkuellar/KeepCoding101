# a list is a collection which is ordered and changeable. Allows duplicate members.

# Create list

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Using a constructor

numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# get a single value

print(fruits[1])

# get length

print(len(fruits))

# append to list

fruits.append('Mangos')

print(fruits)

# remove from list

fruits.remove('Grapes')

print(fruits)

# insert into position

fruits.insert(2, 'Strawberries')

print(fruits)

# change value

fruits[0] = 'Blueberries'

print(fruits)

# remove with pop

fruits.pop(2)

print(fruits)

# reverse list

fruits.reverse()

print(fruits)

# sort list

fruits.sort()

print(fruits)

# reverse sort

fruits.sort(reverse=True)

print(fruits)


