import random
import os
from colorama import init, Fore, Style
import time
import sys

# Initialize Colorama for colored output
init()

def int_input(prompt, selection):
    x = input(prompt)
    while not x.isnumeric() or not int(x) in selection:
        if x.lower() == "quit":
            print("The game has been forced quit. Have a nice day!")
            quit()
        else:
            x = input(prompt)
    return int(x)


def computer_win():


    print(f"   ___                            _              __    __ _           ")
    print(f"  / __\___  _ __ ___  _ __  _   _| |_ ___ _ __  / / /\ \ (_)_ __  ___ ")
    print(f" / /  / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| \ \/  \/ / | '_ \/ __|")
    print(f"/ /__| (_) | | | | | | |_) | |_| | ||  __/ |     \  /\  /| | | | \__ \ ") 
    print(f"\____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \/  \/ |_|_| |_|___/")
    print(f"                     |_|                                              ")

    print(Fore.YELLOW+"                            .-=========-.")
    print(Fore.YELLOW+"                            \'-=======-'/")
    print(Fore.YELLOW+"                            _|   .=.   |_")
    print(Fore.YELLOW+"                           ((|  {{1}}  |))")
    print(Fore.YELLOW+"                            \|   /|\   |/")
    print(Fore.YELLOW+"                             \__ '`' __/")
    print(Fore.YELLOW+"                               _`) (`_" )
    print(Fore.YELLOW+"                             _/_______\_")
    print(Fore.YELLOW+"                            /___________\ ")

def player_win():
    print("   ___ _                          __    __ _           ")
    print("  / _ \ | __ _ _   _  ___ _ __   / / /\ \ (_)_ __  ___ ")
    print(" / /_)/ |/ _` | | | |/ _ \ '__|  \ \/  \/ / | '_ \/ __|")
    print("/ ___/| | (_| | |_| |  __/ |      \  /\  /| | | | \__ \ ")
    print("\/    |_|\__,_|\__, |\___|_|       \/  \/ |_|_| |_|___/")
    print("               |___/                                  ")
    
    
    print(Fore.YELLOW+"                      .-=========-.")
    print(Fore.YELLOW+"                      \'-=======-'/")
    print(Fore.YELLOW+"                       |   .=.   |_")
    print(Fore.YELLOW+"                     ((|  {{1}}  |))")
    print(Fore.YELLOW+"                      \|   /|\   |/")
    print(Fore.YELLOW+"                       \__ '`' __/")
    print(Fore.YELLOW+"                         _`) (`_" )
    print(Fore.YELLOW+"                       _/_______\_")
    print(Fore.YELLOW+"                      /___________\ ")
    
# Function to create and display the battle grid
def battleGrid(displayGrid,row_list,col_list):
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
def player_shoot(displayGrid,coordGrid,col_list,row_list):
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

def computer_shoot(row_list,col_list,displayGrid,coordGrid):
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
def user_turn(displayGrid,coordGrid,random_num3,random_num4,row_list,col_list):
    
    print("User Objective:\nSink The Computer's Ship In Five Turns")
    
    battleGrid(displayGrid,row_list,col_list)
    player_shoot(displayGrid,coordGrid,col_list,row_list)

    # Check if player hits ship 1 or ship 2
    if coordGrid[random_num3][random_num4] == "x":
        print("You sunk the Computer's ship! You WIN!")
        player_win()
        print(Fore.WHITE+"Back To Menu In 5 Seconds")
        time.sleep(5)
        game()
        
        
    os.system('cls' if os.name == 'nt' else 'clear')


# Function for manual ship placement
def computer_turn(displayGrid,coordGrid,row1,col1,row_list,col_list):

    print("Computer Objective:\nSink The User's Ship In Five Turns")
    # printship(s)

    battleGrid(displayGrid,row_list,col_list)
    computer_shoot(row_list,col_list,displayGrid,coordGrid)

    # Check if player hits ship 1 or ship 2
    if coordGrid[row1][col1] == "x":
        print("Computer sunk your ship! Better luck next time.")
        computer_win()
        print(Fore.WHITE+"Back To Menu In 5 Seconds")
        time.sleep(5)
        game()

    os.system('cls' if os.name == 'nt' else 'clear')

                
# Function to display the ship placement grid
def shipPlaceGrid(shipPlaceDisplayGrid,col_list,row_list):
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
def game():
    os.system('cls' if os.name == 'nt' else 'clear')


    print(Fore.WHITE +"Welcome to Battleship!")
    print(Fore.RED +   " ______           _     _   __                __        _                                                         ___#_#___|__")                                         
    print(Fore.RED +   "|_   _ \         / |_  / |_[  |              [  |      (_)                                                    _  |____________|  _")                            
    print(Fore.RED +   "  | |_) |  ,--. `| |-'`| |-'| | .---.  .--.   | |--.   __  _ .--.                                    =====| |.---------------------------. | |====")                            
    print(Fore.WHITE + "  |  __'. `'_\ : | |   | |  | |/ /__\\( (`\]  | .-. | [  |[ '/'`\ \                <--------------------'   .  .  .  .  .  .  .  .   '--------------/")                        
    print(Fore.WHITE + " _| |__) |// | |,| |,  | |, | || \__., `'.'.  | | | |  | | | \__/ |                 __..._____--==/___]_|__|__________________________________[___\==--____,------_' .7")                   
    print(Fore.BLUE + f"|_______/ \'-;__/\__/  \__/[___]'.__.'[\__) )[___]|__][___]| ;.__/                 |                                                                            BB-61/")               
    print(Fore.BLUE+ f"                                                           [__|                    \_______________________________________________USS:______________________________/")


    print(f"""{Fore.RED}Description:
    {Fore.LIGHTBLACK_EX}    The game starts with a 5x5 grid displayed on the screen.
        You will be prompted to input the coordinates where you want to shoot.
        Coordinates should be in the format X,# (e.g., A,1).
        If your shot hits the ship, you win and the game ends.
        If your shot misses, you can try again.
        The game will update the grid after each shot to reflect the shots fired.
    {Fore.RED}    Please enter \"Quit\" at any time to end the game.\n""")

    print(Fore.WHITE+"Create Your Grid:")


# EDGE CASES!!
    col_list = int_input(Fore.BLUE+"    How many columns (max 26): ", range(0, 27))

    row_list = int_input("    How many rows (max 26): ", range(0, 27))



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
    shipPlaceGrid(shipPlaceDisplayGrid,row_list,col_list)

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
    shipPlaceGrid(shipPlaceDisplayGrid,col_list,row_list)

    while True:
        computer_turn(displayGrid, coordGrid,row1,col1,row_list,col_list)
        user_turn(displayGrid,coordGrid,random_num3,random_num4,row_list,col_list)
        
game()