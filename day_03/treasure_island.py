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
print("Your mission is to find the treasure.")

print("\nYou're standing at the island's entrance.")
print("Choose your direction:")

print("1. North (jungle)")
print("2. East (rocky coastline)")
print("3. West (rickety bridge)")

direction = int(input("\nChoose direction (1/2/3): "))

if direction == 1:
    print("You get lost in the dense jungle. Game Over.")

elif direction == 3:
    print("You cross the bridge, but it collapses! Game Over")

elif direction == 2:
    print("You find a hidden cave with a river flowing into it.")

    print("\nChoose transport:")
    print("1. Boat")
    print("2. Swim")

    transport = int(input("Choose Transport (1/2): "))

    if transport == 2:
        print("Strong currents sweep you away. Game Over.")

    elif transport == 1:
        print("You safely cross the river and find a hidden passage.")
        print("After moving forward you found a treasure.")

        print("\nChoose a colored key to unlock the treasure")
        print("1. Red")
        print("2. Green")
        print("3. Blue")

        color = int(input("\nChoose a color (1/2/3): "))

        if color == 3:
            print("Correct color! You unlock the chest and find the treasure. You Win!")
        else:
            print("Wrong color! Treasure remains hidden. Game Over.")

else:
    print("Invalid option. Try again")
