print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.\n")

path = input("Left or right?").lower()

if path == "left" or path == " left":
    print("You've come to a large body of water.  Will you swim or wait?\n")
    step = input().lower()
    if step == "wait":
        print("a mysterious cloaked figure approaches with a raft and takes you across the pond.\n On the other side is a castle with 3 doors, one Red, one Yellow, and one Blue.  What is the color of the door you choose?")
        door = input()
        if door == "yellow":
            print("Congratulations!  You found the hidden treasure.")
        elif door == "blue":
            print("You've been eaten by beasts.  You're dead.")
        elif door == "red":
            print("You've been blasted by a wall of mortal flame.  You're dead.")
        else:
            print("You didn't find the treasure.  Game over.")
    else:
        print("You've been eaten by pirhanna.  You're dead.")
else:
    print("Fall into a hole. Game over")