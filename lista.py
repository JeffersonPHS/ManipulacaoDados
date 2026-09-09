fruits = ["apple", "banana"]
fruits.append("cherry")      # ['apple', 'banana', 'cherry']
# ['apple', 'banana', 'cherry', 'mango', 'fig']
fruits.extend(["mango", "fig"])
fruits.insert(1, "orange")

items = ["A", "B", "C", "B"]
items.pop(0)       # Removes and returns 'A' -> ['B', 'C', 'B']
items.remove("B")  # Removes first 'B' -> ['C', 'B']
del items[1]       # Deletes index 1 -> ['C']
items.clear()      # Empty list -> []

letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])   # ['b', 'c', 'd']
print(letters[::-1])  # ['e', 'd', 'c', 'b', 'a']

# Double only the even numbers in a range
evens_doubled = [x * 2 for x in range(6) if x % 2 == 0]
# Output: [0, 4, 8]
