from colorama import init, Fore

def board():
    # Get number of columns and rows from user
    col_list = int(input("How many columns: "))
    if col_list >= 27:
        while col_list>= 27:
            col_list = int(input("Too many Maximum Col Is 26 How many columns: "))

    row_list = int(input("How many rows: "))
    if row_list >= 27:
        while row_list>= 27:
            row_list = int(input("Too many Maximum Row Is 26 How many columns: "))

    # Create the grid with empty spaces
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

board()
