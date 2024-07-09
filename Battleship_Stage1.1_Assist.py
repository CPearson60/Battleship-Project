# import random
# import os
# from colorama import init, Fore, Style

# # Initialize Colorama for colored output
# init()

# # Function to create and display the battle grid
# def battleGrid(displayGrid):
#     # Print letters for columns header
#     print("", Fore.LIGHTCYAN_EX + "|", " ", end="")
#     for col in range(col_list):
#         if col + 1 == 1:
#             print(f"{col + 1}", end="  |")
#         else:
#             if col < 9:
#                 print(f"  {col + 1}", end="  |")
#             else:
#                 print(f" {col + 1}", end="  |")
#     print("")

#     # Print grid rows
#     for i in range(row_list):
#         print(Fore.LIGHTCYAN_EX + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
#         for j in range(col_list):
#             print(displayGrid[i][j], end="   | ")  # Print grid content
#         print()

# # Function for player to shoot
# def player_shoot():
#     while True:
#         shot = input("Where do you want to shoot? (A-E,1-{}): ".format(col_list)).strip().replace(",", "")
#         if len(shot) == 2 and shot[0].lower() in ["a", "b", "c", "d", "e"] and shot[1].isdigit() and int(shot[1]) <= col_list:
#             break
#         else:
#             print("Invalid input. Please enter a valid coordinate (A-E,1-{}).".format(col_list))

#     row = ord(shot[0].lower()) - ord('a')
#     col = int(shot[1]) - 1

#     X = "x"
#     displayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX} {X} {Fore.LIGHTCYAN_EX}"
#     coordGrid[row][col] = X

#     return (displayGrid, coordGrid, X)

# # Function for computer to place ships
# def computer_ship_place():
#     # Initialize ship positions randomly
#     random_num1 = random.randint(0, row_list - 1)
#     random_num2 = random.randint(0, col_list - 1)
#     random_num3 = random.randint(0, row_list - 1)
#     random_num4 = random.randint(0, col_list - 1)

#     while random_num1 == random_num3 and random_num2 == random_num4:
#         random_num3 = random.randint(0, row_list - 1)
#         random_num4 = random.randint(0, col_list - 1)

#     ship1 = (random_num1, random_num2)
#     ship2 = (random_num3, random_num4)

#     while True:
#         battleGrid(displayGrid)
#         player_shoot()
#         os.system('cls' if os.name == 'nt' else 'clear')

#         if (random_num1, random_num2) == (row, col):
#             print("You hit a ship!")
#         elif (random_num3, random_num4) == (row, col):
#             print("You hit a ship!")

#         if (random_num1, random_num2) == (row, col) and (random_num3, random_num4) == (row, col):
#             print("Both ships have been sunk. You win!")
#             break

# # Function to display the ship placement grid
# def shipPlaceGrid(shipPlaceDisplayGrid):
#     # Print letters for columns header
#     print("", Fore.LIGHTCYAN_EX + "|", " ", end="")
#     for col in range(col_list):
#         if col + 1 == 1:
#             print(f"{col + 1}", end="  |")
#         else:
#             if col < 9:
#                 print(f"  {col + 1}", end="  |")
#             else:
#                 print(f" {col + 1}", end="  |")
#     print("")

#     # Print grid rows
#     for i in range(row_list):
#         print(Fore.LIGHTCYAN_EX + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
#         for j in range(col_list):
#             print(shipPlaceDisplayGrid[i][j], end="   | ")  # Print grid content
#         print()

# # Function for manual ship placement
# def manual_ship_place():
#     # Display initial ship placement grid
#     shipPlaceGrid(shipPlaceDisplayGrid)

#     # Input for ship 1
#     while True:
#         ship1 = input("Please enter the coordinate for your first ship (A-E,1-{}): ".format(col_list)).strip().replace(",", "")
#         if len(ship1) == 2 and ship1[0].lower() in ["a", "b", "c", "d", "e"] and ship1[1].isdigit() and int(ship1[1]) <= col_list:
#             break
#         else:
#             print("Invalid input. Please enter a valid coordinate (A-E,1-{}).".format(col_list))

#     row1 = ord(ship1[0].lower()) - ord('a')
#     col1 = int(ship1[1]) - 1

#     # Mark ship on shipPlaceGrid
#     shipPlaceDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"
#     shipPlaceGrid(shipPlaceDisplayGrid)

#     # Input for ship 2
#     while True:
#         ship2 = input("Please enter the coordinate for your second ship (A-E,1-{}): ".format(col_list)).strip().replace(",", "")

#         # Check if ship 2 is not placed on the same spot as ship 1
#         if ship2 == ship1:
#             print("A ship has already been placed there. Please enter a different coordinate (A-E,1-{}).".format(col_list))
#             continue

#         if len(ship2) == 2 and ship2[0].lower() in ["a", "b", "c", "d", "e"] and ship2[1].isdigit() and int(ship2[1]) <= col_list:
#             break
#         else:
#             print("Invalid input. Please enter a valid coordinate (A-E,1-{}).".format(col_list))

#     row2 = ord(ship2[0].lower()) - ord('a')
#     col2 = int(ship2[1]) - 1

#     # Mark ship on shipPlaceGrid
#     shipPlaceDisplayGrid[row2][col2] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"
#     os.system('cls' if os.name == 'nt' else 'clear')

#     # Start the battle
#     while True:
#         battleGrid(displayGrid)
#         player_shoot()

#         # Check if player hits ship 1 or ship 2
#         if (row1, col1) == (row, col):
#             print("You hit a ship!")
#         elif (row2, col2) == (row, col):
#             print("You hit a ship!")

#         # Check if both ships have been sunk
#         if (row1, col1) == (row, col) and (row2, col2) == (row, col):
#             print("Both ships have been sunk. You win!")
#             break

# # Function to choose ship placement method
# def ship_place_method():
#     while True:
#         ship_placement = input("""Do you want to manually place the ships or 
# have the computer randomly generate ship placement?

# 0 - Manual
# 1 - Computer
# Enter 0 or 1: """).strip()

#         if ship_placement == "0":
#             os.system('cls' if os.name == 'nt' else 'clear')
#             manual_ship_place()
#             break
#         elif ship_placement == "1":
#             os.system('cls' if os.name == 'nt' else 'clear')
#             computer_ship_place()
#             break
#         else:
#             print("Invalid input. Please enter either 0 or 1.")

# # Welcome message and grid size input
# print("Welcome to Battleship!")
# col_list = int(input("How many columns (max 26): "))
# while col_list >= 27:
#     col_list = int(input("Too many. Maximum columns is 26. How many columns: "))

# row_list = int(input("How many rows (max 26): "))
# while row_list >= 27:
#     row_list = int(input("Too many. Maximum rows is 26. How many rows: "))

# # Initialize grids
# displayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
# coordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
# shipPlaceDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

# # Start ship placement method selection
# ship_place_method()





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
    displayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX} {X} {Fore.LIGHTCYAN_EX}"
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

    ship1 = (random_num1, random_num2)
    ship2 = (random_num3, random_num4)

    while True:
        battleGrid(displayGrid)
        player_shoot()
        os.system('cls' if os.name == 'nt' else 'clear')

        if (random_num1, random_num2) == (row, col):
            print("You hit a ship!")
        elif (random_num3, random_num4) == (row, col):
            print("You hit a ship!")

        if (random_num1, random_num2) == (row, col) and (random_num3, random_num4) == (row, col):
            print("Both ships have been sunk. You win!")
            break

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
        ship1 = input("Please enter the coordinate for your first ship (A-E,1-{}): ".format(col_list)).strip().replace(",", "")
        if len(ship1) == 2 and ship1[0].lower() in ["a", "b", "c", "d", "e"] and ship1[1].isdigit() and int(ship1[1]) <= col_list:
            break
        else:
            print("Invalid input. Please enter a valid coordinate (A-E,1-{}).".format(col_list))

    row1 = ord(ship1[0].lower()) - ord('a')
    col1 = int(ship1[1]) - 1

    # Mark ship on shipPlaceGrid
    shipPlaceDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"
    shipPlaceGrid(shipPlaceDisplayGrid)

    # Input for ship 2
    while True:
        ship2 = input("Please enter the coordinate for your second ship (A-E,1-{}): ".format(col_list)).strip().replace(",", "")

        # Check if ship 2 is not placed on the same spot as ship 1
        if ship2 == ship1:
            print("A ship has already been placed there. Please enter a different coordinate (A-E,1-{}).".format(col_list))
            continue

        if len(ship2) == 2 and ship2[0].lower() in ["a", "b", "c", "d", "e"] and ship2[1].isdigit() and int(ship2[1]) <= col_list:
            break
        else:
            print("Invalid input. Please enter a valid coordinate (A-E,1-{}).".format(col_list))

    row2 = ord(ship2[0].lower()) - ord('a')
    col2 = int(ship2[1]) - 1

    # Mark ship on shipPlaceGrid
    shipPlaceDisplayGrid[row2][col2] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"
    os.system('cls' if os.name == 'nt' else 'clear')

    # Start the battle
    while True:
        battleGrid(displayGrid)
        player_shoot()

        # Check if player hits ship 1 or ship 2
        if (row1, col1) == (row, col):
            print("You hit a ship!")
        elif (row2, col2) == (row, col):
            print("You hit a ship!")

        # Check if both ships have been sunk
        if (row1, col1) == (row, col) and (row2, col2) == (row, col):
            print("Both ships have been sunk. You win!")
            break

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
