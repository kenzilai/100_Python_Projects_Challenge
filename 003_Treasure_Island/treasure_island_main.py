print('''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
crossroad = input("You\'re at a crossroad, type 'left' to go left or 'right' to go right?\n").lower()
if crossroad == "left":
    lake = input("You came to a lake and saw an island in the middle of the lake, type 'swim' to swim across or type 'wait' to wait for a boat\n").lower()
    if lake == "wait":
        print("You saw three doors.")
        door = input("Which door you choose? Red, Yellow or Blue?\n").lower()
        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("You chose a door that doesn't exist.\nGame Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fell into a hole.\nGame Over.")