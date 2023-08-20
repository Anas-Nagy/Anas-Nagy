x = input("input:")
y = ["a", "e", "i", "o", "u", "O"]
for char in x:
 for vowels in y:
  x = x.replace(vowels, "")
print(x)
