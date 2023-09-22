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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print("Welcome to the treasure island!")
print("Your mission is to find the One Piece.")
first_choice = input("Which way you want to choose? Left or Right.")
direction = first_choice.lower()

if direction == "left":
    second_choice = input(
        "Now you see a vast sea. Do you want to swim across or just wait for a lift? Swim or Wait")
    swim_wait = second_choice.lower()
    if swim_wait == "swim":
        print("Game over!!! A'you mental? Who swim across the SEA. Anyways you got eaten by a Shark.")
        print('''                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\
            -David "TAZ" Baltazar-
          ''')
    elif swim_wait == "wait":
        print('''
     __/\__
  ~~~\____/~~~~~~
    ~  ~~~   ~.         b'ger
              ''')
        third_choice = input(
            "After a while you got a lift and you reached a house. Now you see three doors. Which one you want to step in? Red or Blue or Yellow")
        door = third_choice.lower()
        if door == "yellow":
            print(
                "Alright you win!! You found the treasure. Horrayyy😪😴. Now can I sleep???🛌")

print("Game over!. Bye Bye!!. Tata!!!. Finish!!!!. Idk why i just want to finish this challenge. Its already 3am in the morning and i cannot be creative this time. I am sleepy right now, so dont ask stupid questions. Accept your faith🤷‍♂️or try another option.")
