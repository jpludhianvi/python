age = 38
name = "Ankit"
weight = 58.5

print(age)
print(name)
print(weight)

#-------------------------------------------------------------------------------

price = 100
tax = 18
total_price = price + tax

print(total_price) 	# Output: 118

#-------------------------------------------------------------------------------
x = 10
y = "geek"
z = 20
w = z

print(x, y, z, w)	# Output: 10 geek 20 20


#-------------------------------------------------------------------------------
x = 10
print(x)	# Output: 10

x = "Python"
print(x)	# Output: Python

#-------------------------------------------------------------------------------
is_valid = True
is_published = False

print(is_valid)			# Output: True
print(is_published)		# Output: False

#-------------------------------------------------------------------------------

x = 100
y = 200

# Pythonic swapping
x, y = y, x

#-------------------------------------------------------------------------------

x, y, z = 100, "Geeks", 10.5

print(x)  # Output: 100
print(y)  # Output: Geeks
print(z)  # Output: 10.5

#-------------------------------------------------------------------------------

print(id(5))  # Unique identifier for the object with value 5
a = 10
print(id(a))  # Unique identifier for the object with value 10
b = a
print(id(b))  # Same identifier as a because both refer to the same object

a = 10
b = 10
print(id(a))  # Identifier for the object with value 10
print(id(b))  # Same identifier as a because a and b refer to the same object

#-------------------------------------------------------------------------------

g = [1, 2, 3]
print(type(g)) # Output: <class 'list'>

c = 2 + 4j
print(type(c))	# Output: <class 'complex'>
