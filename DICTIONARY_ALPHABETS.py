#A Python program to print a dictionary whose keys should be the alphabet from a-z and
# the value should be corresponding ASCII values

d = {}
for i in range(97,123): 
    d[chr(i)] = i
print(d)
