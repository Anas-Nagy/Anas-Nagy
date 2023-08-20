valid_number = [25, 10, 5]

x = int(input("insert coin: "))
if x in valid_number:
    while x != 50:
        print(f"Amount Due: {50 - x}")
        x = x + int(input("insert coin: "))
        if x >= 50:
            break
else:
    print("Amount Due: 50")
change = x - 50
if x > 50:
        print(f"Change Owed: {change}")
else:

 print("Change Owed: 0")