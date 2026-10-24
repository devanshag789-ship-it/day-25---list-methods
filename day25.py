# Day 25: Useful list methods

fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print("After insert:", fruits)

print("Index of banana:", fruits.index("banana"))
print("Count of banana:", fruits.count("banana"))

numbers = [5, 6, 7, 3, 2, 1, 0, 9, 7, 4, 5]
numbers.sort(reverse=True)
print("Sorted descending:", numbers)

values = [1, 2, 3, 8, 6, 9, 5]
values.reverse()
print("Reversed:", values)

original = [1, 2, 3]
copied = original.copy()
copied[2] = 100
print("Original:", original)
print("Copy changed:", copied)

a = [1, 2]
b = [3, 4]
a.extend(b)
print("Extended a:", a)
print("Unchanged b:", b)

temporary = ["remove", "all", "items"]
temporary.clear()
print("After clear:", temporary)
