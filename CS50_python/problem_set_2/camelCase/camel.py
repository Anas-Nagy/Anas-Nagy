Camel_case = input("Enter: ").strip()
x = Camel_case
for i in range(len(Camel_case)):
    if Camel_case[i].isupper():
        x = x.replace(Camel_case[i], ("_"+ Camel_case[i]))
x = x.lower()
print(x)
