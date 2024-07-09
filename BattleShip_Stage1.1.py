import random
import os
from colorama import init, Fore, Style

# 5x5 grid
coordGrid = [
["A1", "A2", "A3", "A4", "A5"],
["B1", "B2", "B3", "B4", "B5"],
["C1", "C2", "C3", "C4", "C5"],
["D1", "D2", "D3", "D4", "D5"],
["E1", "E2", "E3", "E4", "E5"]
]
# battleGrid seperate list (stores coords and mimics displayGrid)
displayGrid = [
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "]
]

# separate grid for displaying
shipPlaceDisplayGrid = [
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "]
]

random_num1 = random.randint(0,4)
random_num2 = random.randint(0,4)
random_num3 = random.randint(0,4)
random_num4 = random.randint(0,4)

while True:
    if random_num1 == random_num3:
        if random_num2 == random_num4:
            random_num3 = random.randint(0,4)
            random_num4 = random.randint(0,4)
    break

from colorama import init, Fore

def board(col_list, row_list):
    # Create the grid with empty spaces
    # displayGrid = 
    displayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

    # Print the top border


    # Print letters for columns header
    print("", Fore.LIGHTCYAN_EX + "|"," ", end="")
    for col in range(col_list):
        if col + 1 == 1:
            print(f"{col+1}",end="  |")
        else:
            if col < 9:
                print(f"  {col+1}",end="  |")
            else:
                print(f" {col+1}",end="  |")
    print("")

    # Print grid rows
    for i in range(row_list):
        print(Fore.LIGHTCYAN_EX + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...) #Chr 6
        for j in range(col_list):
            print(displayGrid[i][j], end="   | ")  # Print grid content
        print()




def battleGrid(displayGrid):
    
    # prints the grid
    print("\n   1     2     3     4     5")
    print("A " + Fore.LIGHTCYAN_EX + f"{displayGrid[0][0]} | {displayGrid[0][1]} | {displayGrid[0][2]} | {displayGrid[0][3]} | {displayGrid[0][4]}")
    print(Fore.LIGHTCYAN_EX + "  ----+-----+-----+-----+----")
    print(Style.RESET_ALL + "B " + Fore.LIGHTCYAN_EX + f"{displayGrid[1][0]} | {displayGrid[1][1]} | {displayGrid[1][2]} | {displayGrid[1][3]} | {displayGrid[1][4]}")
    print(Fore.LIGHTCYAN_EX + "  ----+-----+-----+-----+----")
    print(Style.RESET_ALL + "C " + Fore.LIGHTCYAN_EX + f"{displayGrid[2][0]} | {displayGrid[2][1]} | {displayGrid[2][2]} | {displayGrid[2][3]} | {displayGrid[2][4]}")
    print(Fore.LIGHTCYAN_EX + "  ----+-----+-----+-----+----")
    print(Style.RESET_ALL + "D " + Fore.LIGHTCYAN_EX + f"{displayGrid[3][0]} | {displayGrid[3][1]} | {displayGrid[3][2]} | {displayGrid[3][3]} | {displayGrid[3][4]}")
    print(Fore.LIGHTCYAN_EX + "  ----+-----+-----+-----+----")
    print(Style.RESET_ALL + "E " + Fore.LIGHTCYAN_EX + f"{displayGrid[4][0]} | {displayGrid[4][1]} | {displayGrid[4][2]} | {displayGrid[4][3]} | {displayGrid[4][4]}\n")
    print(Style.RESET_ALL)

    return coordGrid, displayGrid


def shipPlaceGrid(shipPlaceDisplayGrid):
    
    board(col_list,row_list)

    return coordGrid, shipPlaceDisplayGrid


def player_shoot():
    shot = input("Where do you want to shoot? (X,#): ").strip()
    shot = shot.replace(",","")
    valid = len(shot) == 2 and shot[0].lower() in ["a", "b", "c", "d","e"] and shot[1] in ["1", "2", "3", "4", "5"] 
    while not valid:
        shot = input("Invalid input. Please enter a valid coordinate (X,#): ").strip()
        shot = shot.replace(",","")
        valid = len(shot) == 2 and shot[0].lower() in ["a", "b", "c", "d","e"] and shot[1] in ["1", "2", "3", "4", "5"] 
    row_convert = {"a":0, "b":1, "c":2, "d":3, "e":4}
    row = row_convert[shot[0].lower()]

    col = int(shot[1]) - 1
    
    X = "x"
    displayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX} {X} {Fore.LIGHTCYAN_EX}"
    coordGrid[row][col] = X
    
    return (displayGrid,coordGrid, X)


def computer_ship_place():
    # computer ships are:
    # ship 1
    # ship 2

    while True: 
        ship1 = coordGrid[random_num1][random_num2]
        ship2 = coordGrid[random_num3][random_num4]
        battleGrid(displayGrid)
        player_shoot()
        os.system('cls' if os.name == 'nt' else 'clear')
        if ship1 == "x":
            print("You hit a ship!")
        elif ship2 == "x":
            print("You hit a ship!")
        
        if ship1 == "x" and ship2 == "x":
            print("Both ships have been sunk. You win!")
            break


def manual_ship_place():
    # manual ships are:
    # ship 3
    # ship 4

    # display initial grid
    shipPlaceGrid(displayGrid)

    # input for ship 3 
    ship3 = input("Please enter the coord for your first ship (X,#): ").strip().replace(",", "")
    while len(ship3) != 2 or ship3[0].lower() not in ["a", "b", "c", "d", "e"] or ship3[1] not in ["1", "2", "3", "4", "5"]:
        ship3 = input("Invalid input. Please enter a valid coordinate (X,#): ").strip().replace(",", "")
    row_convert = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    row1 = row_convert[ship3[0].lower()]
    col1 = int(ship3[1]) - 1

    # mark shipPlaceGrid
    displayGrid[row1][col1] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"
    # display updated grid
    shipPlaceGrid(displayGrid)

    # input for ship 4
    ship4 = input("Please enter the coord for your second ship (X,#): ").strip().replace(",", "")

    # placing ship 4 in the same spot as ship 3 edge case
    while ship4 == ship3:
            ship4 = input("A ship has already been placed there. Please enter a different coordinate (X,#): ").strip().replace(",", "")


    while len(ship4) != 2 or ship4[0].lower() not in ["a", "b", "c", "d", "e"] or ship4[1] not in ["1", "2", "3", "4", "5"]:
        ship4 = input("Invalid input. Please enter a valid coordinate (X,#): ").strip().replace(",", "")
    row2 = row_convert[ship4[0].lower()]
    col2 = int(ship4[1]) - 1

    # mark shipPlaceGrid
    shipPlaceDisplayGrid[row2][col2] = f"{Fore.LIGHTRED_EX} O {Fore.LIGHTCYAN_EX}"

    # clear the board to play
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        battleGrid(displayGrid)
        player_shoot()

        # check if player hits ship 3 or ship 4
        if coordGrid[row1][col1] == "x":
            print("You hit a ship!")
        elif coordGrid[row2][col2] == "x":
            print("You hit a ship!")
        
        # check if both ships have been sunk
        if coordGrid[row1][col1] == "x" and coordGrid[row2][col2] == "x":
            print("Both ships have been sunk. You win!")
            break


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


# Get number of columns and rows from user
col_list = int(input("How many columns: "))
if col_list >= 27:
    while col_list>= 27:
        col_list = int(input("Too many Maximum Col Is 26 How many columns: "))

row_list = int(input("How many rows: "))
if row_list >= 27:
    while row_list>= 27:
        row_list = int(input("Too many Maximum Row Is 26 How many columns: "))

board(col_list,row_list)
print("Welcome to Battleship!") 
ship_place_method()
