list1 = [33,324,422543262646354346243542534444]

set1 = set(list1)
print(list1)
print()
print(set1)

if 33 in set1:
    print("this number exists in the set")
else:
    print("this number does not exist in the set")

food = set([])
food.add(371)
food.add(371)
food.add(23345)
print(food)

set1.remove(33)
print(set1)

setA = {432567,7980,356,5627}
setB = {534,4366986,8904809,63556,363834,37983938,40,356,43256}
print("\nresult of union operatin\n")
print(setA.union(setB))
print(setB | setA)
print("\nresult of intrsection operation\n")
print(setA.intersection(setB))
print(setB & setA)
print("\nresult of difference operation\n")
print(setA.difference(setB)) 
print(setB - setA)
print("\nresult of symetric_difference operation\n")
print(setA.symmetric_difference(setB))
print(setB ^ setA)