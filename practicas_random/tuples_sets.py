# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) # Using a constructor


# Single value needs trailing comma
fruits2 = ('Apples',)  # This is not a tuple, it's a string

# Get a single value

print(fruits[1])

# Can't change value

#fruits[0] = 'Pears'

# Delete tuple

del fruits2

print(len(fruits))

#print(fruits, fruits2)

# A set is a collection which is unordered and unindexed. No duplicate members.

# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set

print('Apples' in fruits_set)

# Add to set

fruits_set.add('Grape')

print(fruits_set)

# Remove from set

fruits_set.remove('Grape')

print(fruits_set)

# Clear set

fruits_set.clear()

print(fruits_set)

# Delete set

del fruits_set

print(fruits_set) # This will throw an error because the set no longer exists
