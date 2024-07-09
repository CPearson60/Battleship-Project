import random
from colorama import init, Fore, Style

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
    
    X = "X"
    displayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX} {X} {Fore.LIGHTCYAN_EX}"
    coordGrid[row][col] = X

    
    return (displayGrid,coordGrid, X)

# 5x5 grid
coordGrid = [
["A1", "A2", "A3", "A4", "A5"],
["B1", "B2", "B3", "B4", "B5"],
["C1", "C2", "C3", "C4", "C5"],
["D1", "D2", "D3", "D4", "D5"],
["E1", "E2", "E3", "E4", "E5"],
]
# battleGrid seperate list (stores coords and mimics displayGrid)
displayGrid = [
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],
["   ","   ","   ","   ","   "],

]
    
# print("Welcome to Battleship!") 
# random_num1 = random.randint(0,4)
# random_num2 = random.randint(0,4)
# ship = coordGrid[random_num1][random_num2]
# print (random_num1,random_num2)
# while True: 
#     battleGrid(displayGrid)
#     player_shoot()
#     if ship == "x":
#         print("You hit the ship!")
#         break


random_num1 = random.randint(0,4)
random_num2 = random.randint(0,4)
print(random_num1,random_num2)
win=False
while win == False:
    if displayGrid[random_num1][random_num2] == "X":
        print("won")
    else:
        battleGrid(displayGrid)
        player_shoot()
        if displayGrid[random_num1][random_num2] == "X":
            win=True
            print(win)