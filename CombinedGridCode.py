import random, os, time
from colorama import init, Fore, Style

def BattleGrid(grid, computerDisplayGrid, playerDisplayGrid, row_list, col_list):
    # Print nums for columns header
    print("", Fore.BLUE + "|", " ", end="")
    for col in range(col_list):
        if col + 1 == 1:
            print(f"{col + 1}", end="  |")
        else:
            #adds space for formating
            if col < 9:
                print(f"  {col + 1}", end="  |")
            # does not inlcude space to format double digits better
            else:
                print(f" {col + 1}", end="  |")
    print("")
    # Print grid rows
    # Chr() function returns a string representing a character whose Unicode code point is the integer specified.
    # Chr(65) = Capital(A)
    for i in range(row_list):
        print(Fore.BLUE + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        if turn == 0:
            for j in range(col_list):
                print(computerDisplayGrid[i][j], end="   | ")  # Print grid content
            print()
        else:
            for j in range(col_list):
                print(playerDisplayGrid[i][j], end="   | ")  # Print grid content
            print()
            
def main():
    row_list=10
    col_list=10
 


main()