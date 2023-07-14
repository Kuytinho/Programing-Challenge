array = ["a", 10, "b", "hello", 122, 15]

letters = [item for item in array if isinstance(item, str)]
numbers = [item for item in array if isinstance(item, int)]

max_number = max(numbers)

print("Array de letras:", letters)
print("Array de números:", numbers)
print("Maior número:", max_number)
