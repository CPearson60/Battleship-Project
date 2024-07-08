import random
from colorama import init, Fore, Style

def battleGrid():
    
    # 5x5 grid
    displayGrid = [
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    
    ]

    # battleGrid seperate list (stores coords and mimics displayGrid)
    coordGrid = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"],
    ["C1", "C2", "C3", "C4", "C5"],
    ["D1", "D2", "D3", "D4", "D5"],
    ["E1", "E2", "E3", "E4", "E5"],
    ]

    # prints the grid
    print(Fore.LIGHTCYAN_EX + f"\n{displayGrid[0][0]} | {displayGrid[0][1]} | {displayGrid[0][2]} | {displayGrid[0][3]} | {displayGrid[0][4]}")
    print("----+-----+-----+-----+----")
    print(Fore.LIGHTCYAN_EX + f"{displayGrid[1][0]} | {displayGrid[1][1]} | {displayGrid[1][2]} | {displayGrid[1][3] | {displayGrid[1][4]}}")
    print("----+-----+-----+-----+----")
    print(Fore.LIGHTCYAN_EX + f"{displayGrid[2][0]} | {displayGrid[2][1]} | {displayGrid[2][2]} | {displayGrid[2][3] | {displayGrid[2][4]}}")
    print("----+-----+-----+-----+----")
    print(Fore.LIGHTCYAN_EX + f"{displayGrid[3][0]} | {displayGrid[3][1]} | {displayGrid[3][2]} | {displayGrid[3][3] | {displayGrid[3][4]}}")
    print("----+-----+-----+-----+----")
    print(Fore.LIGHTCYAN_EX + f"{displayGrid[4][0]} | {displayGrid[4][1]} | {displayGrid[4][2]} | {displayGrid[4][3] | {displayGrid[4][4]}}\n")
    print(Style.RESET_ALL)

battleGrid()