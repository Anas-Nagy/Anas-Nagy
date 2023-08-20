answer = input("answer of the Question: ").strip()
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("yes")
elif answer == "FoRty TwO".strip():
    print("yes")
else:
    print("no")