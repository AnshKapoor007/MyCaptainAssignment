set1 = {int(item) for item in input("Enter first set elements: ").split()} #Taking set1 from user
set2 = {int(item) for item in input("Enter second set elements: ").split()} #Taking set2 from user

print("Set1: " , set1)
print("Set2: " , set2)

print("Union of both sets: " , set1.union(set2)) #Printing their union
print("Intersection of both sets: " , set1.intersection(set2)) #Printing their intersection
print("Difference of set1 from set2: " , set1.difference(set2)) #Printing their difference
print("Symmetric difference of set1 from set2: " , set1.symmetric_difference(set2)) #Printing their symmetric difference