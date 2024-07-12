import random
import os
from colorama import init, Fore, Style

# Initialize Colorama for colored output
init()


# Function to create and display the battle grid
def playerBattleGrid(playerDisplayGrid):
    # Print letters for columns header
    print("", Fore.BLUE + "|", " ", end="")
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
        print(Fore.BLUE + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        for j in range(col_list):
            print(playerDisplayGrid[i][j], end="   | ")  # Print grid content
        print()


def computerBattleGrid(computerDisplayGrid):
    # Print letters for columns header
    print("", Fore.BLUE + "|", " ", end="")
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
        print(Fore.BLUE + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        for j in range(col_list):
            print(computerDisplayGrid[i][j], end="   | ")  # Print grid content
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
    computerDisplayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX}{X}{Fore.BLUE}"
    coordGrid[row][col] = X
    return (computerDisplayGrid, coordGrid, X)


# Function for computer to shoot


# Function for computer to place ships
def computer_ship_place():
    # Initialize ship positions randomly
    random_num1 = random.randint(0, row_list - 1)
    random_num2 = random.randint(0, col_list - 1)

    n=0
    while True:
        print("Computer Objective:\nSink The User's Ship In Five Turns")

        if n>4:
            print("Computer Loses! You WIN!")
            break
        else:
            playerBattleGrid(playerDisplayGrid)
            player_shoot()

            # Check if player hits ship 1 or ship 2
            if coordGrid[random_num1][random_num2] == "x":
                print("Computer sunk the ship! Better luck next time.")
                break
            n+=1
            os.system('cls' if os.name == 'nt' else 'clear')
                

# Function to display the ship placement grid for USER
def shipPlaceGrid(shipPlaceDisplayGrid):
    # Print letters for columns header
    print("", Fore.BLUE + "|", " ", end="")
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
        print(Fore.BLUE + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        for j in range(col_list):
            print(shipPlaceDisplayGrid[i][j], end="   | ")  # Print grid content
        print()



# Function for manual ship placement and player turn
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
    shipPlaceDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
    shipPlaceGrid(shipPlaceDisplayGrid)


    n=0
    while True:
        print("Objective:\nSink The Computer's Ship In Five Turns")
        # printship(s)
        if n>4:
            print("Computer wins! Better luck next time.")
            break
        else:
            computerBattleGrid(computerDisplayGrid)
            player_shoot()

            # Check if player hits ship 1 or ship 2
            if coordGrid[row1][col1] == "x":
                print("You sunk the ship! You win!")
                break  # Mark ship 1 as sunk
            n+=1
            os.system('cls' if os.name == 'nt' else 'clear')










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
playerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
computerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
coordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
shipPlaceDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

# prompt user to place their ship
manual_ship_place()