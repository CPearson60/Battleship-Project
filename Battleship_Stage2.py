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
        shot = input(f"Where do you want to shoot (A-{chr(65 + row_list - 1)},1-{col_list})? ").strip().replace(",", "")
        if shot.lower() == "quit":
            print("The game has been forced quit. Have a nice day!")
            quit()
        elif len(shot) >= 2 and shot[0].upper() in [chr(65 + i) for i in range(row_list)] and shot[1:].isdigit() and int(shot[1:]) <= col_list:
            break
        else:
            print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

    # generate shot coordinates
    row = ord(shot[0].upper()) - ord('A')
    col = int(shot[1:]) - 1

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
    
    print("User Objective:\nSink The Computer's Ship In Five Turns")
    
    battleGrid(displayGrid)
    player_shoot()

    # Check if player hits ship 1 or ship 2
    if coordGrid[random_num3][random_num4] == "x":
        print("You sunk the Computer's ship! You WIN!")
        quit()
    os.system('cls' if os.name == 'nt' else 'clear')


# Function for manual ship placement
def computer_turn():

    print("Computer Objective:\nSink The User's Ship In Five Turns")
    # printship(s)

    battleGrid(displayGrid)
    computer_shoot()

    # Check if player hits ship 1 or ship 2
    if coordGrid[row1][col1] == "x":
        print("Computer sunk your ship! Better luck next time.")
        quit()  # Mark ship 1 as sunk

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



# Welcome message and grid size input

os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to Battleship!")


print(Fore.RED +   " ______           _     _   __                __        _                                                         ___#_#___|__")                                         
print(Fore.RED +   "|_   _ \         / |_  / |_[  |              [  |      (_)                                                    _  |____________|  _")                            
print(Fore.RED +   "  | |_) |  ,--. `| |-'`| |-'| | .---.  .--.   | |--.   __  _ .--.                                    =====| |.---------------------------. | |====")                            
print(Fore.WHITE + "  |  __'. `'_\ : | |   | |  | |/ /__\\( (`\]  | .-. | [  |[ '/'`\ \                <--------------------'   .  .  .  .  .  .  .  .   '--------------/")                        
print(Fore.WHITE + " _| |__) |// | |,| |,  | |, | || \__., `'.'.  | | | |  | | | \__/ |                 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")                   
print(Fore.BLUE +  "|_______/ \'-;__/\__/  \__/[___]'.__.'[\__) )[___]|__][___]| ;.__/                 |                                                                     BB-61/")               
print(Fore.BLUE +  "                                                           [__|                    \_______________________________________________WWS______________________/")

print("Please enter \"Quit\" at any time to end the game.")

col_list = (input("How many columns (max 26): "))

try:
    if col_list.lower() == "quit":
                print("The game has been forced quit. Have a nice day!")
                quit()
    else:
        col_list = int(col_list) 

    while col_list >= 27:
        col_list = (input("Too many. Maximum columns is 26. How many columns: "))
        if col_list.lower() == "quit":
                print("The game has been quit. Have a nice day!")
                quit()
        else:
            col_list = int(col_list) 

    row_list = (input("How many rows (max 26): "))
    if row_list.lower() == "quit":
                print("The game has been forced quit. Have a nice day!")
                quit()
    else:
        row_list = int(row_list) 

    while row_list >= 27:
        row_list = (input("Too many. Maximum rows is 26. How many rows: "))
        if row_list.lower() == "quit":
                print("The game has been forced quit. Have a nice day!")
                quit()
        else:
            row_list = int(row_list) 
except:
     print("Invalid input. Please enter a valid input.")

alphabet_lower = [] 
for i in range(row_list):
        letter = chr(ord('a') + i)  # Get the ASCII character corresponding to 'a' + i
        alphabet_lower.append(letter)

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
    if ship1.lower() == "quit":
        print("The game has been forced quit. Have a nice day!")
        quit()
    elif len(ship1) >= 2 and ship1[0].upper() in [chr(65 + i) for i in range(row_list)] and ship1[1:].isdigit() and int(ship1[1:]) <= col_list:
        break
    else:
        print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

# generates coords of the user ship
row1 = ord(ship1[0].upper()) - ord('A')
col1 = int(ship1[1:]) - 1

# Initialize ship positions for computer randomly
random_num3 = random.randint(0, row_list - 1)
random_num4 = random.randint(0, col_list - 1)

# Mark ship on shipPlaceGrid
shipPlaceDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.LIGHTCYAN_EX}"
shipPlaceGrid(shipPlaceDisplayGrid)

while True:
    computer_turn()
    user_turn()