lst = ['Apple', 'Guava', 'Mango','Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:",lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated list", lst)

lst.remove('Guava')
print("Updated list", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop(1)
print("Updated list:", lst)

lst.reverse()
print("Reversed list:", lst)

print("Multiplication on List:", lst*2)

lst = lst[:4]
print("Sliced list")

lst.clear()
print("Updated list", lst)
