# ==================================================
# DAY 2 - PYTHON FUNDAMENTALS
# ==================================================


# ==================================================
# 1. VARIABLES
# ==================================================

# A variable is a named container used to store a value.

a = 5

# type() function is used to identify the data type
# of a variable or value.

print(type(a))


# ==================================================
# 2. PRIMARY DATA TYPES
# ==================================================

# int     - Whole numbers
# float   - Decimal numbers
# bool    - True or False values
# str     - Text or strings

a = 5
b = 3.5
c = True
d = "Python"

print(type(a))  # int
print(type(b))  # float
print(type(c))  # bool
print(type(d))  # str


# ==================================================
# 3. VARIABLE NAMING CONVENTIONS
# ==================================================

# 1. Variable names should not contain spaces.
# 2. Variable names should begin with a letter or underscore.
# 3. Variable names cannot begin with a number.
# 4. Variable names can contain letters, numbers and underscores.
# 5. Variable names are case-sensitive.
# 6. Use meaningful names for better readability.

student_name = "John"
age = 21
total_marks = 450

# Invalid variable names:
# student name = "John"
# 1student = "John"


# ==================================================
# 4. COLLECTIONS IN PYTHON
# ==================================================

# Collections are used to store multiple values
# in a single variable.

# Four important collection data types:
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary


# ==================================================
# 4.1 LIST
# ==================================================

# List is an ordered collection.
# Lists are mutable (changeable).
# Lists allow duplicate values.
# Lists support positive and negative indexing.

brands = ["Zara", "HM", "Nike", "Puma", "Puma1"]

# Display the entire list
print(brands)

# len() returns the total number of elements in the list
print(len(brands))


# --------------------------------------------------
# LIST INDEXING
# --------------------------------------------------

# Positive indexing starts from 0.
# Negative indexing starts from -1 (last element).

print(brands[0])   # First element
print(brands[2])   # Third element
print(brands[-1])  # Last element


# --------------------------------------------------
# LIST METHODS
# --------------------------------------------------

# 1. APPEND()
# Adds a single element at the end of the list.

brands.append("Converse")
print(brands)


# 2. INSERT()
# Inserts an element at a specific index.
# The remaining elements are shifted to the right.

brands.insert(2, "Jordan")
print(brands)


# 3. EXTEND()
# Adds multiple elements from another iterable
# to the end of the existing list.

brands.extend(["VKC", "Asian"])
print(brands)


# 4. REMOVE()
# Removes the first occurrence of the specified value.
# Raises ValueError if the element is not present.

brands.remove("Puma")
print(brands)


# 5. POP()
# Removes an element using its index.
# If no index is provided, removes the last element.

brands.pop(1)
print(brands)


# 6. UPDATING A LIST ELEMENT
# Lists are mutable, so we can change an element
# directly using its index.

brands[1] = "HM"
print(brands)


# ==================================================
# 4.2 TUPLE
# ==================================================

# Tuple is an ordered collection.
# Tuples are immutable (unchangeable).
# Tuples allow duplicate values.
# Tuples support indexing.

vehicles = ("Car", "Bike")

print(vehicles)
print(type(vehicles))


# --------------------------------------------------
# TUPLE IMMUTABILITY
# --------------------------------------------------

# We cannot directly modify an element in a tuple.
# The following statement will raise a TypeError.

# vehicles[1] = "Truck"


# --------------------------------------------------
# CREATING A TUPLE WITH ONE ELEMENT
# --------------------------------------------------

# A comma is mandatory when creating a single-element tuple.

colors = ("red",)

print(type(colors))


# --------------------------------------------------
# ADDING ELEMENTS TO A TUPLE
# --------------------------------------------------

# Tuples are immutable, so we cannot directly add elements.
# However, we can achieve this in two ways.


# METHOD 1: CONVERT TUPLE INTO LIST

# Step 1: Convert the tuple into a list.
vehicle_list = list(vehicles)

# Step 2: Add a new element.
vehicle_list.append("Lorry")

# Step 3: Convert the list back into a tuple.
vehicles = tuple(vehicle_list)

print(vehicles)


# METHOD 2: COMBINE TWO TUPLES

# We can combine two tuples using the + operator.

vehicles2 = ("Bus", "Pickup Truck")

vehicles = vehicles + vehicles2

# Shorthand for the above statement:
# vehicles += vehicles2

print(vehicles)


# ==================================================
# 4.3 SET
# ==================================================

# Set is an unordered collection.
# Sets do not allow duplicate elements.
# Sets do not support indexing.
# Individual elements cannot be modified after insertion.
# However, we can add or remove elements.

fruits = {"apple", "banana", "cherry", "cherry"}

# Duplicate values are automatically removed.
print(fruits)


# --------------------------------------------------
# ACCESSING SET ELEMENTS
# --------------------------------------------------

# Sets do not support indexing.
# We can access their elements using a for loop.

for element in fruits:
    print(element)


# --------------------------------------------------
# CHECKING WHETHER AN ELEMENT EXISTS
# --------------------------------------------------

# The 'in' operator checks whether an element is present.

if "apple" in fruits:
    print("Apple is available")


# --------------------------------------------------
# NOT IN OPERATOR
# --------------------------------------------------

# The 'not in' operator checks whether an element is absent.

if "orange" not in fruits:
    print("Orange is not available")


# --------------------------------------------------
# SET METHODS
# --------------------------------------------------

# 1. ADD()
# Adds a single element to the set.

fruits.add("dragonfruit")
print(fruits)


# 2. UPDATE()
# Adds multiple elements from an iterable to the set.

fruits.update({"kiwi", "pineapple"})
print(fruits)


# 3. REMOVE()
# Removes the specified element.
# Raises KeyError if the element is not present.

fruits.remove("dragonfruit")
print(fruits)


# 4. POP()
# Removes and returns an arbitrary element from the set.
# Since sets are unordered, we cannot predict which
# element will be removed.

fruits.pop()
print(fruits)


# 5. DISCARD()
# Removes the specified element.
# Unlike remove(), discard() does not raise an error
# if the element is not present.

fruits.discard("apple")
print(fruits)


# ==================================================
# 4.4 DICTIONARY
# ==================================================

# Dictionary stores data in key-value pairs.
# Dictionaries are ordered (insertion order is maintained).
# Dictionaries are mutable (changeable).
# Duplicate keys are not allowed.
# Values can be duplicated.

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2025,
    "year": 2026
}

# When duplicate keys are provided,
# the latest value replaces the previous value.

print(car)


# --------------------------------------------------
# CREATING A DICTIONARY USING dict() CONSTRUCTOR
# --------------------------------------------------

# dict() constructor can also be used to create a dictionary.
# Here, keys are passed as keyword arguments.

car2 = dict(
    brand="Mercedes Benz",
    model="CLR AMG",
    year=2001
)

print(car2)


# --------------------------------------------------
# ACCESSING DICTIONARY VALUES
# --------------------------------------------------

# METHOD 1: USING SQUARE BRACKETS
# Access a value by specifying its key.
# Raises KeyError if the key does not exist.

print(car["brand"])


# METHOD 2: USING get() METHOD
# Accesses a value using its key.
# Returns None if the key does not exist by default.

print(car.get("brand"))


# --------------------------------------------------
# DICTIONARY METHODS
# --------------------------------------------------

# 1. KEYS()
# Returns all the keys present in the dictionary.

print(car.keys())


# 2. UPDATING AN EXISTING VALUE
# We can update a value by referring to its key.

car["year"] = 1998
print(car)


# 3. UPDATE()
# Updates an existing key-value pair.
# Can also be used to add new key-value pairs.

car.update({"year": 2020})
print(car)


# 4. ADDING NEW ELEMENTS
# Assigning a value to a new key adds a new key-value pair.

car["color"] = "red"
print(car)


# 5. POP()
# Removes the specified key-value pair.

car.pop("brand")
print(car)


# 6. POPITEM()
# Removes the last inserted key-value pair.
# Dictionaries maintain insertion order in Python 3.7+.

car.popitem()
print(car)