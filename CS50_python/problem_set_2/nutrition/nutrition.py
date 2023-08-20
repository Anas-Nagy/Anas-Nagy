x = input("Item:").title().strip()
food = {
      "Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90,
      "HoneydewMelon": 50, "Kiwifruit": 90, "Lemon": 15, "Lime": 15, "Nectarine": 60, "Orange": 80, "Peach": 60,
      "Pear": 100, "Pineapple": 50, "Plums": 70, "Strawberries": 50, "Tangerine": 50,  # This is line 18
      "Watermelon": 80 ,"Sweet Cherries": 100
  }
print(x)
if x in food:
     print(food[x])