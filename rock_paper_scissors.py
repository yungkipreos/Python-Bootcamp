# Rock, paper, scissors game
a = input("Player One: ")
b = input("Player Two: ")

rules = {'rock': 1, 'paper': 2, 'scissors': 3}

if (a not in rules or b not in rules):
    print("Not an option!")
a = rules[str(a)]
b = rules[str(b)]

a = int(a)
b = int(b)

# Game rules
if (a - b == 0):
    print ("Congrats! It's a tie.")
if (a > b):
    print ("Player One wins!")
if (a < b):
    print ("Player Two wins!")