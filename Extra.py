import random

ship_point_grid = coordGrid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]

displayGrid = [
    ["   ","   ","   ","   ","   "],
    ["   ","   ","   ","   ","   "],
    ["   ","   ","   ","   ","   "],
    ["   ","   ","   ","   ","   "],
    ["   ","   ","   ","   ","   "]
    
    ]

def random_num():
    return random.randint(0,4)
   

def ship_point(ship_point_grid):
    
    ship_point_grid[random_num][random_num] = 1
    print(ship_point_grid)
    
random_num=random_num()

ship_point(ship_point_grid)

# Used To Associate 
A=0
B=1
C=2
D=3
E=4


def player_shoot():
    
    shot = input("Where do you want to shoot? [column][row]: ").strip()
    valid = len(shot) == 2 and shot[0].lower() in ["a", "b", "c", "d","e"] and shot[1] in ["1", "2", "3", "4", "5"]
    while not valid:
        Shot = input("Wrong format, input [column],[row]: ").strip()
        valid = len(shot) == 2 and shot[0].lower() in ["a", "b", "c", "d","e"] and shot[1] in ["1", "2", "3", "4", "5"]
    row_convert = {"a":0, "b":1, "c":2, "d":3, "e":4}
    row = row_convert[shot[0].lower()]

    col = int(shot[1]) - 1
    
    displayGrid[row][col] = "x"
    print(displayGrid)
    return (row, col)

player_shoot()