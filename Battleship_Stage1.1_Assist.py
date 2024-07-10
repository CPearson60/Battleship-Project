import random
import os
from colorama import init, Fore, Style

# Initialize Colorama for colored output
init()

def printship(s):
    
    if s == 0:
        print(Fore.WHITE+f"             # #  ( )                           # #  ( )  ")
        print(Fore.WHITE+f"          ___#_#___|__                       ___#_#___|__")                                         
        print(Fore.WHITE+f"      _  |____________|  _               _  |____________|  _")                                                                           
        print(Fore.WHITE+f" _-==/___]_|__|____[___\==--___ .7  _-==/___]_|__|____[___\==--___ .7")                   
        print(Fore.WHITE+f"|                          BB-61/  |                          BB-61/")               
        print(Fore.WHITE+f"\______________________________/   \______________________________/")  
        print(Fore.WHITE+"\n______________________________________________________________________\n")

    if s == 1:
        print(Fore.WHITE+f"             # #  ( )     ")
        print(Fore.WHITE+f"          ___#_#___|__")                                         
        print(Fore.WHITE+f"      _  |____________|  _")                                                                           
        print(Fore.WHITE+f" _-==/___]_|__|____[___\==--___ .7")                   
        print(Fore.WHITE+f"|                          BB-61/")               
        print(Fore.WHITE+f"\______________________________/")
        
    if s == 2:
        print("you win")


# Function to create and display the battle grid
def battleGrid(displayGrid):
    # Print letters for columns header
    print("", Fore.LIGHTCYAN_EX + "|", " ", end="")
    for col in range(col_list):
        if col + 1 == 1:
            print(f"{col + 1}", end="  |")
        else:
            if col < 9:
                print(f"  {col + 1}", end="  |")
            else:
                print(f" {col + 1}", end="  |")
    print("")

    # Print grid rows
    for i in range(row_list):
        print(Fore.LIGHTCYAN_EX + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        for j in range(col_list):
            print(displayGrid[i][j], end="   | ")  # Print grid content
        print()

# Function for player to shoot
def player_shoot():
    while True:
        shot = input("Where do you want to shoot? (A-E,1-{}): ".format(col_list)).strip().replace(",", "")
        if len(shot) == 2 and shot[0].lower() in ["a", "b", "c", "d", "e"] and shot[1].isdigit() and int(shot[1]) <= col_list:
            break
        else:
            print("Invalid input. Please enter a valid coordinate (A-E,1-{}).".format(col_list))

    row = ord(shot[0].lower()) - ord('a')
    col = int(shot[1]) - 1

    X = "x"
    displayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX}{X}{Fore.LIGHTCYAN_EX}"
    coordGrid[row][col] = X
    return (displayGrid, coordGrid, X)

# Function for computer to place ships
def computer_ship_place():
    # Initialize ship positions randomly
    random_num1 = random.randint(0, row_list - 1)
    random_num2 = random.randint(0, col_list - 1)
    random_num3 = random.randint(0, row_list - 1)
    random_num4 = random.randint(0, col_list - 1)

    while random_num1 == random_num3 and random_num2 == random_num4:
        random_num3 = random.randint(0, row_list - 1)
        random_num4 = random.randint(0, col_list - 1)

    # Initialize variables to track whether ships are sunk
    ship1_sunk = False
    ship2_sunk = False
    n=0
    s=0
    while True:
        print("Objective:\nSink The Ships In Five Turns")
        printship(s)

        if n>5:
            print("You Lose")
            break
        else:
            battleGrid(displayGrid)
            player_shoot()

            # Check if player hits ship 1 or ship 2
            if coordGrid[random_num1][random_num2] == "x":
                print("You hit ship 1!")
                s=1
                ship1_sunk = True  # Mark ship 1 as sunk
            if coordGrid[random_num3][random_num4] == "x":
                print("You hit ship 2!")
                ship2_sunk = True  # Mark ship 2 as sunk
                s=2

            # Check if both ships have been sunk
            if ship1_sunk and ship2_sunk:
                print("Both ships have been sunk. You win!")
                break
            n+=1
            os.system('cls' if os.name == 'nt' else 'clear')
                
# Function to display the ship placement grid
def shipPlaceGrid(shipPlaceDisplayGrid):
    # Print letters for columns header
    print("", Fore.LIGHTCYAN_EX + "|", " ", end="")
    for col in range(col_list):
        if col + 1 == 1:
            print(f"{col + 1}", end="  |")
        else:
            if col < 9:
                print(f"  {col + 1}", end="  |")
            else:
                print(f" {col + 1}", end="  |")
    print("")

    # Print grid rows
    for i in range(row_list):
        print(Fore.LIGHTCYAN_EX + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        for j in range(col_list):
            print(shipPlaceDisplayGrid[i][j], end="   | ")  # Print grid content
        print()

# Function for manual ship placement
def manual_ship_place():

    # Display initial ship placement grid
    shipPlaceGrid(shipPlaceDisplayGrid)

    # Input for ship 1
    while True:
        ship1 = input(f"Please enter the coordinate for your first ship (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")
        if len(ship1) >= 2 and ship1[0].upper() in [chr(65 + i) for i in range(row_list)] and ship1[1:].isdigit() and int(ship1[1:]) <= col_list:
            break
        else:
            print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

    row1 = ord(ship1[0].upper()) - ord('A')
    col1 = int(ship1[1:]) - 1

    # Mark ship on shipPlaceGrid
    shipPlaceDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.LIGHTCYAN_EX}"
    shipPlaceGrid(shipPlaceDisplayGrid)

    # Input for ship 2
  
    while True:

        ship2 = input(f"Please enter the coordinate for your second ship (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")

        # Check if ship 2 is not placed on the same spot as ship 1
        if ship2.upper() == ship1.upper():
            print("A ship has already been placed there. Please enter a different coordinate.")
            continue

        if len(ship2) >= 2 and ship2[0].upper() in [chr(65 + i) for i in range(row_list)] and ship2[1:].isdigit() and int(ship2[1:]) <= col_list:
            break
        else:
            print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

            
    row2 = ord(ship2[0].upper()) - ord('A')
    col2 = int(ship2[1:]) - 1

    # Mark ship on shipPlaceGrid
    shipPlaceDisplayGrid[row2][col2] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"
    os.system('cls' if os.name == 'nt' else 'clear')

    # Initialize variables to track whether ships are sunk
    ship1_sunk = False
    ship2_sunk = False
    n=0
    while True:
        print("Objective:\nSink The Ships In Five Turns")

        if n>5:
            print("You Lose")
            break
        else:
            battleGrid(displayGrid)
            player_shoot()

            # Check if player hits ship 1 or ship 2
            if coordGrid[row1][col1] == "x":
                print("You hit ship 1!")
                ship1_sunk = True  # Mark ship 1 as sunk
            if coordGrid[row2][col2] == "x":
                print("You hit ship 2!")
                ship2_sunk = True  # Mark ship 2 as sunk

            # Check if both ships have been sunk
            if ship1_sunk and ship2_sunk:
                print("Both ships have been sunk. You win!")
                break
            n+=1
# Function to choose ship placement method
def ship_place_method():
    while True:
        ship_placement = input("""Do you want to manually place the ships or 
have the computer randomly generate ship placement?

0 - Manual
1 - Computer
Enter 0 or 1: """).strip()

        if ship_placement == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            manual_ship_place()
            break
        elif ship_placement == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            computer_ship_place()
            break
        else:
            print("Invalid input. Please enter either 0 or 1.")

# Welcome message and grid size input
print("Welcome to Battleship!")

os.system('cls' if os.name == 'nt' else 'clear')
s=0
print(Fore.RED +   " ______           _     _   __                __        _                                                         ___#_#___|__")                                         
print(Fore.RED +   "|_   _ \         / |_  / |_[  |              [  |      (_)                                                    _  |____________|  _")                            
print(Fore.RED +   "  | |_) |  ,--. `| |-'`| |-'| | .---.  .--.   | |--.   __  _ .--.                                    =====| |.---------------------------. | |====")                            
print(Fore.WHITE + "  |  __'. `'_\ : | |   | |  | |/ /__\\( (`\]  | .-. | [  |[ '/'`\ \                <--------------------'   .  .  .  .  .  .  .  .   '--------------/")                        
print(Fore.WHITE + " _| |__) |// | |,| |,  | |, | || \__., `'.'.  | | | |  | | | \__/ |                 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")                   
print(Fore.BLUE +  "|_______/ \'-;__/\__/  \__/[___]'.__.'[\__) )[___]|__][___]| ;.__/                 |                                                                     BB-61/")               
print(Fore.BLUE +  "                                                           [__|                    \_______________________________________________WWS______________________/")


col_list = int(input("How many columns (max 26): "))
while col_list >= 27:
    col_list = int(input("Too many. Maximum columns is 26. How many columns: "))

row_list = int(input("How many rows (max 26): "))
while row_list >= 27:
    row_list = int(input("Too many. Maximum rows is 26. How many rows: "))

# Initialize grids
displayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
coordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
shipPlaceDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

# Start ship placement method selection
ship_place_method()
