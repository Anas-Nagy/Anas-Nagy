x = input("Item:").title.strip
food = {
      "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
      "honeydewmelon": 50, "kiwifruit": 90, "lemon": 15, "lime": 15, "nectarine": 60, "orange": 80, "peach": 60,
      "pear": 100, "pineapple": 50, "plums": 70, "strawberries": 50, "tangerine": 50,
      "sweet cherries": 100,
      "watermelon": 80
  }

if x in food:
     print(food[x])