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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_choice = input("You find yourself at a crossroads, which way do you want to go? Type left or right to choose.\n")

if first_choice.lower() == "left":
  second_choice = input("You've made the right choice adventurer, you now find yourself at a river. It's waters are raging would you like to wait for a boat or swim across? Type wait or swim to choose.\n")
  if second_choice.lower() == "wait":
    third_choice = input("You've safely crossed the river! You find old ruins just ahead as you enter the ruins you see three doors before you, one blue, one red and one yellow. Which will you choose? Type red, blue or yellow to choose")
    if third_choice.lower() == "blue":
      print("You are overcome by savage beasts and are torn apart. Game Over.")
    elif third_choice.lower() == "red":
      print("You enter a room of eternal flames and are burnt to a crisp instantly. Game Over.")
    elif third_choice.lower() == "yellow":
      print("You enter the old ruins legendary treasure chest! You will be rich beyond your wildest dreams! Well done adventurer and good game.")
    else:
      print("Unsure of what to do, a group of Harpies scoop you up into the sky, Game Over.")
  else:
    print("You've leaped into the water, braving it's cold when suddenly a stinging whip pierces your ankle. You begin to lose consciousness your body grows weak as you drift down the river. Game Over.")
else:
  print("You've fallen into a sinkhole! I'm sorry adventurer this will be your end.")