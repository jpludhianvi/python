#Lists

a = [10, 20, 30, 40, 50]
print(a)
print(a[0])
print(a[1])
print(a[:4])
print(a[:3])
print(id(a[0]))
print(id(a[1]))
print(id(a))


a = [10, 20, 30, 40, 50]
print(a)	  # Output: [10, 20, 30, 40, 50]
print(a[3])   # Output: 40
print(a[-1])  # Output: 50
print(a[-2])  # Output: 40

a.insert(2,22)
print(a)
print(15 in a)  # Output: True
print(40 in a)  # Output: False
print(a.count(10))
print(a.index(30))

b = [10, 20, 30, 40, 50]
print(max(b))  # Output: 50
print(min(b))  # Output: 10
print(sum(b))  # Output: 150

b.sort()
print(b)	# Output: [10, 20, 30, 40, 50]

b.reverse()
print(b)	# Output: [50, 40, 30, 20, 10]

#----------------------------------------------------------------------
#Tuples
my_tuple = (10, 20, 'geek')
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: geek
my_tuple[0] = 30  # This will raise an error
# With parentheses
a = (10, 20, 'geek')

# Without parentheses
a = 10, 20, 'geek'

# Single-item tuple
b = (10,)

print(len(a))  # Output: 3

nested_tuple = (10, 'geek', (1, 2, 3))
print(nested_tuple[2])        # Output: (1, 2, 3)
print(nested_tuple[2][1])     # Output: 2
print(a.count(10))  # Output: 1
print(a.index(10))


#----------------------------------------------------------------------
#Sets

s1 = {10, 20, 30}
print(s1)			# Output: {10, 20, 30}

s2 = set([20, 30, 40])
print(s2)			# Output: {40, 20, 30}

s3 = {}
print(type(s3))		# Output: <class 'dict'>

s4 = set()
print(type(s4))  	# Output: <class 'set'>
print(s4)        	# Output: set()

s = {10, 20}
s.add(30)
print(s)  		# Output: {10, 20, 30}

s.add(30)
print(s)  		# Output: {10, 20, 30}

s.update([40, 50])
print(s)  		# Output: {40, 10, 50, 20, 30}

s = {10, 30, 20, 40}
s.discard(30)
print(s)  		# Output: {10, 20, 40}

s.remove(20)
print(s)  		# Output: {40, 10}

s.clear()
print(s)  		# Output: set()

s.add(50)
del s
# After del s, accessing s will raise an error

s = {10, 30, 20, 40}
print(len(s))       # Output: 4
print(20 in s)      # Output: True
print(50 in s)      # Output: False

s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

print(s1 | s2)          # Output: {2, 3, 4, 6, 8, 9}
print(s1 & s2)          # Output: {6}
print(s1 - s2)          # Output: {2, 4, 8}
print(s1 ^ s2)          # Output: {2, 3, 4, 8, 9}

s1 = {2, 4, 6, 8}
s2 = {4, 8}

print(s1.isdisjoint(s2))  # Output: False
print(s1 <= s2)           # Output: False
print(s1 < s2)            # Output: False
print(s1 >= s2)           # Output: True
print(s1 > s2)            # Output: True

