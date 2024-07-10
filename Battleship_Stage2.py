import random
import os
from colorama import init, Fore, Style

# Initialize Colorama for colored output
init()


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

def computer_shoot():
    random_num1 = random.randint(0, row_list - 1)
    random_num2 = random.randint(0, col_list - 1)
        
    row = random_num1
    col = random_num2
    print(f"Computer shoots at {random_num1},{random_num2}")

    X = "x"
    displayGrid[row][col] = f"{Fore.LIGHTMAGENTA_EX}{X}{Fore.LIGHTCYAN_EX}"
    coordGrid[row][col] = X
    return (displayGrid, coordGrid, X)


# Function for computer to place ships
def user_turn():
    
    n=0
    print("User Objective:\nSink The Computer's Ship In Five Turns")

    if n>4:
        print("You missed every shot! Better luck next time.")
        quit()
    else:
        battleGrid(displayGrid)
        player_shoot()

        # Check if player hits ship 1 or ship 2
        if coordGrid[random_num3][random_num4] == "x":
            print("You sunk the Computer's ship! You WIN!")
            quit()
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
def computer_turn():

    n=0

    print("Computer Objective:\nSink The User's Ship In Five Turns")
    # printship(s)
    if n>4:
        print("Computer missed every shot! You WIN!")
        quit()
    else:
        battleGrid(displayGrid)
        computer_shoot()

        # Check if player hits ship 1 or ship 2
        if coordGrid[row1][col1] == "x":
            print("Computer sunk your ship! Better luck next time.")
            quit()  # Mark ship 1 as sunk
        n+=1
        # os.system('cls' if os.name == 'nt' else 'clear')



# Welcome message and grid size input

os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to Battleship!")


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
# Display initial ship placement grid
shipPlaceGrid(shipPlaceDisplayGrid)

# Input for user ship
while True:
    ship1 = input(f"Please enter the coordinate for your ship (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")
    if len(ship1) >= 2 and ship1[0].upper() in [chr(65 + i) for i in range(row_list)] and ship1[1:].isdigit() and int(ship1[1:]) <= col_list:
        break
    else:
        print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

row1 = ord(ship1[0].upper()) - ord('A')
col1 = int(ship1[1:]) - 1

# Initialize ship positions for computer randomly
random_num3 = random.randint(0, row_list - 1)
random_num4 = random.randint(0, col_list - 1)

# Mark ship on shipPlaceGrid
shipPlaceDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.LIGHTCYAN_EX}"
shipPlaceGrid(shipPlaceDisplayGrid)

n=0
while True:
    computer_turn()
    user_turn()