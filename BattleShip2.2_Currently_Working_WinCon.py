import random
import os
from colorama import init, Fore, Style
import time
from ship_animations import shipanimation

# Initialize Colorama for colored output
init()

#Ginna

def int_input(prompt, selection):#This function accounts for edge cases and used to force quit game
    x = input(prompt)
    while not x.isnumeric() or not int(x) in selection:# repeats prompt until satisfactory input
        
        if x.lower() == "quit": # force quits if the player inputs "quit"
            print("The game has been forced quit. Have a nice day!")
            quit()
        else:
            x = input(prompt)
    return int(x)

# Cameron
def BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list): # This fuction is used to create a visual board *List of List
    print("", Fore.BLUE + "|", " ", end="")# Print nums for columns header
    for col in range(col_list): 
        if col + 1 == 1:
            print(f"{col + 1}", end="  |")
        else:
            if col < 9:
                print(f"  {col + 1}", end="  |")#adds space for formating
           
            else:
                print(f" {col + 1}", end="  |") # does not inlcude space to format double digits better
    print("")
    # Print grid rows
    # Chr() function returns a string representing a character whose Unicode code point is the integer specified.
    # Chr(65) = Capital(A)
    for i in range(row_list):
        print(Fore.BLUE + f"{chr(65 + i)}|", end=" ")  # Print row letters (A, B, C, ...)
        if turn == 1:
            for j in range(col_list):
                print(computerDisplayGrid[i][j], end="   | ")  # Print grid content
            print()
        else:
            for j in range(col_list):
                print(playerDisplayGrid[i][j], end="   | ")  # Print grid content
            print()
    
def Shoot_Guess(computerDisplayGrid, computerCoordGrid, col_list, row_list,turn): # This Fuction Control The Shooting Logic
    while True:
        if turn == 0: # Logic For Comptuter Choosing Point To Shoot
            shot = (f" {chr(random.randint(65, 65 + row_list - 1) )}{random.randint(1,col_list)}").strip().replace(",", "")

        if turn == 1: # Player Coord Input For Choosing Point To Shoot
            shot = input(f"Where do you want to shoot (A-{chr(65 + row_list - 1)},1-{col_list})? ").strip().replace(",", "")
            
        if shot.lower() == "quit": # In The Case PLayer Wants To "Quit" This Is The Logic
            print("The game has been forced quit. Have a nice day!")
            quit()

        elif len(shot) >= 2 and shot[0].upper() in [chr(65 + i) for i in range(row_list)] and shot[1:].isdigit() and int(shot[1:]) <= col_list:# Logic For Checking If The Computer or Player Input Is Valid --- *         #ensures length of character is atleast 2 | checks if first character is valid and within range | ensures character is digit *valid column number coverts & into int*
            break
      
        else: # In Case Where The Input Is Not Valid Player Is Instructed To Input Another Coordinate --- * Computer Logic Always Selects A Valid Coord *
            print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")
            print (shot)

    row = ord(shot[0].upper()) - ord('A')# Converts Letter Given Into An ACSII Value, Which Is Then Subrtacted By The ACSII Value Of A(65) To Generate An Index Value
    col = int(shot[1:]) - 1 # Subtracts Number Given by One To Generate The Correct Index Value

    X = "x"
    computerDisplayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX}{X}{Fore.BLUE}" # Places An "x" wherever player shoots
    computerCoordGrid[row][col] = X
    return (computerDisplayGrid, computerCoordGrid, X)

# Gianna
def Turn_system(turn, playerShips, computerShips, playerDisplayGrid, playerCoordGrid, playerShip1_name, playerShip2_name, computerShip1_name, computerShip2_name, computerDisplayGrid, computerCoordGrid, row1, col1, row2, col2, row3, col3, row4, col4, random1_StartRowCoord, random1_StartColCoord, random2_StartRowCoord, random2_StartColCoord, attachedShip1Row, attachedShip1Col, attachedShip2Row, attachedShip2Col, row_list, col_list): # Function for computer to place ships
    
    if turn == 0: # Computer Turn

        for x, y in playerShips.items(): # prints list of ships and coords for testing
            print(f"- {x}, {y}")

        shipanimation(3) #computer turn text
        Shoot_Guess(playerDisplayGrid, playerCoordGrid,row_list, col_list,turn) # Computer Shoot Guess
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list) # Displays Player Grid 

        if playerCoordGrid[row1][col1] == playerCoordGrid[row2][col2] == playerCoordGrid[row3][col3] == playerCoordGrid[row4][col4] == "x": # Win Check
            print("The computer sunk both your ships! Better luck next time.")
            shipanimation(4) #computer win animation
            t=10
            while t > 0: # Timer Until Goes Back To Menu * Main()*
                print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
                time.sleep(1)  # wait for 1 second
                t -= 1
            main()
            
    
       
        print("Computer Move Log:")
        if playerCoordGrid[row1][col1] == "x":
            print(f"The computer hit your ship, {playerShip1_name}!") # Check if computer hits ship 1
        if playerCoordGrid[row2][col2] == "x":
            print(f"The computer hit your ship, {playerShip1_name}!") # Check if computer hits ship 1
        if playerCoordGrid[row3][col3] == "x":
            print(f"The computer hit your ship, {playerShip2_name}!") # Check if computer hits ship 2
        if playerCoordGrid[row4][col4] == "x":
            print(f"The computer hit your ship, {playerShip2_name}!") # Check if computer hits ship 2

        if playerCoordGrid[row1][col1] == playerCoordGrid[row2][col2] == "x":
            print(f"The computer sunk your ship, {playerShip1_name}!")
        if playerCoordGrid[row3][col3] == playerCoordGrid[row4][col4] == "x":
            print(f"The computer sunk your ship, {playerShip2_name}!")
        else:
            print("The computer missed!")
        t=5
        while t > 0:
            print(f"{Fore.WHITE}Player moves in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
            time.sleep(1)  # wait for 1 second
            t -= 1

        os.system('cls' if os.name == 'nt' else 'clear')
    
    if turn == 1: # Player Turn

        for x, y in computerShips.items(): # prints list of ships and coords for testing
            print(f"- {x}, {y}")
        # Player Turn Text
        shipanimation(2)
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list) # Prints Computer Board
        Shoot_Guess(computerDisplayGrid, computerCoordGrid, col_list, row_list,turn) # Player Shoot Logic
        os.system('cls' if os.name == 'nt' else 'clear')
        shipanimation(2) # Player Turn Text
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

        if computerCoordGrid[random1_StartRowCoord][random1_StartColCoord] == computerCoordGrid[attachedShip1Row][attachedShip1Col] == computerCoordGrid[random2_StartRowCoord][random2_StartColCoord] == computerCoordGrid[attachedShip2Row][attachedShip2Col] == "x":
            print("You sunk both of the computer's ships! You WIN!")
            shipanimation(5)
            t=10
            while t > 0:
                print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
                time.sleep(1)  # wait for 1 second
                t -= 1
            main()

        # Check if player hits ship 1 or ship 2
        print("Player Move Log:")
        if computerCoordGrid[random1_StartRowCoord][random1_StartColCoord] == "x":

            print(f"You hit the Computer's ship, {computerShip1_name}!")
        if computerCoordGrid[attachedShip1Row][attachedShip1Col] == "x":

            print(f"You hit the Computer's ship, {computerShip1_name}!")
        if computerCoordGrid[random2_StartRowCoord][random2_StartColCoord] == "x":

            print(f"You hit the Computer's ship, {computerShip2_name}!")
        if computerCoordGrid[attachedShip2Row][attachedShip2Col] == "x":
            print(f"You hit the Computer's ship, {computerShip2_name}!")

        if computerCoordGrid[random1_StartRowCoord][random1_StartColCoord] == computerCoordGrid[attachedShip1Row][attachedShip1Col] == "x":
            print(f"You sunk the computer's ship, {playerShip1_name}!")
        if computerCoordGrid[random2_StartRowCoord][random2_StartColCoord] == computerCoordGrid[attachedShip2Row][attachedShip2Col] == "x":
            print(f"You sunk the computer's ship, {playerShip2_name}!")
        else:
            print("You missed!")

        
            
        t=5
        while t > 0:
            print(f"{Fore.WHITE}Computer moves in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
            time.sleep(1)  # wait for 1 second
            t -= 1

        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')


def main(): # Everything Runs Off Main Function

#--------------------------Variables To Control game--------------------------#
#_____________________________________________________________________________#
#                                                                             #
    col_list = 10 # Variable To Control Size Of Grid Columns                  #
    row_list = 10 # Variable To Control Size Of Grid Rows                     #
    turn = 0 # Sets Turn To Zero So Player Board Is Shown For Ship Placement  #
#_____________________________________________________________________________#   


    os.system('cls' if os.name == 'nt' else 'clear')   
    
    
    # Battle Ship Welcome Screen/ Menu Screen
    print(Fore.WHITE +"Welcome to Battleship!")
    print(Fore.RED +   " ______           _     _   __                __        _                                                         ___#_#___|__")                                          
    print(Fore.RED +   "|_   _ \         / |_  / |_[  |              [  |      (_)                                                    _  |____________|  _")                             
    print(Fore.RED +   "  | |_) |  ,--. `| |-'`| |-'| | .---.  .--.   | |--.   __  _ .--.                                    =====| |.---------------------------. | |====")                            
    print(Fore.WHITE + "  |  __'. `'_\ : | |   | |  | |/ /__\\( (`\]  | .-. | [  |[ '/'`\ \                <--------------------'   .  .  .  .  .  .  .  .   '--------------/")                        
    print(Fore.WHITE + " _| |__) |// | |,| |,  | |, | || \__., `'.'.  | | | |  | | | \__/ |                 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")                   
    print(Fore.BLUE +  "|_______/ \'-;__/\__/  \__/[___]'.__.'[\__) )[___]|__][___]| ;.___/                 |                                                                     BB-61/")               
    print(Fore.BLUE +  "                                                           [__|                    \_______________________________________________WWS______________________/")

    # Rules For Battleship
    print(f"""{Fore.RED}Description:                                              
    {Fore.LIGHTBLACK_EX}    The game starts with a grid of your choosing displayed on the screen.
        You will be prompted to input the coordinates where you want to shoot.
        Coordinates should be in the format X,# (e.g., A,1).
        If your shot hits the ship, you win and the game ends.
        If your shot misses, you can try again.
        The game will update the grid after each shot to reflect the shots fired.
    {Fore.RED}    Please enter \"Quit\" at any time to end the game.\n""")
    
    print(Fore.WHITE+"Create Your Grid:")
   
    
    # Gianna
    # Initialize grids
    computerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
    computerCoordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

    playerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
    playerCoordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

    # Display initial ship placement grid
    BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

    # Input for player ship 2x1
    playerShips = {} # Player Ship Dictionary

    playerShip1_name = input("Name your first ship: ")

    while True: # Player Ship 1 Logic
        while True:
            while True:
                ship1 = input(f"Please enter the front coordinate for your ship, {playerShip1_name} (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")
                if ship1.lower() == "quit":
                    print("The game has been forced quit. Have a nice day!")
                    quit()
                elif len(ship1) >= 2 and ship1[0].upper() in [chr(65 + i) for i in range(row_list)] and ship1[1:].isdigit() and int(ship1[1:]) <= col_list:
                    break
                else:
                    print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")
            break

        
        # generates coords of the player ship 2x1
        row1 = ord(ship1[0].upper()) - ord('A')
        col1 = int(ship1[1:]) - 1
        playerDisplayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
        
        # asks and defines orientation for 2x1 ship
        orientation = input(f"Choose your ship orientation for {playerShip1_name} (v for vertical, h for horizontal)").strip()
        while True:
            if orientation.lower() != "h" and orientation.lower() != "v" :
                os.system('cls' if os.name == 'nt' else 'clear')
                BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
                orientation = input(f"Choose your ship orientation(v for vertical, h for horizontal)").strip()
            else:
                break
        while True:
            if orientation.lower()=="v":
                if row1 < row_list-1:
                    row2 = row1 + 1
                    col2 = col1 
                    break
                else:
                    row2 = row1 - 1
                    col2 = col1
                    break
            else:
                break
        while True:      
            if orientation.lower()=="h":
                if col1 < col_list-1:
                    row2=row1
                    col2=col1 + 1
                    break
                else:
                    row2=row1
                    col2=col1 - 1
                    break
            else:
                break
        
        playerDisplayGrid[row2][col2] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

        while True:
                satisfied = input(f"Is this where you want {playerShip1_name}? (Y/N) ").strip()
                if satisfied.lower() == "y":
                    break
                elif satisfied.lower() != "n":
                    print(f"Invalid input. Please enter Y or N: ")
                else:
                    playerDisplayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
                    playerCoordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

                    break

        if satisfied.lower() == "y":
            break

    playerShips.update({playerShip1_name: [f"First Coord: ({row1}, {col1})   Second Coord: ({row2}, {col2})"]}) # Adds Ship Name And Coords To Dict

    while True:  # Player Ship 2 Name Logic
        playerShip2_name = input("Name your second ship: ")
        if playerShip2_name == playerShip1_name:
            print("That's already the name of your first ship. Please name your second ship differently.")
        else:
            break

    
    while True: # Player Ship 2 Logic
        while True:
            
            while True:
                ship2 = input(f"Please enter the front coordinate for your ship, {playerShip2_name} (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")
                if ship2.lower() == "quit":
                    print("The game has been forced quit. Have a nice day!")
                    quit()
                elif len(ship2) >= 2 and ship2[0].upper() in [chr(65 + i) for i in range(row_list)] and ship2[1:].isdigit() and int(ship2[1:]) <= col_list:     
                    row3 = ord(ship2[0].upper()) - ord('A')
                    col3 = int(ship2[1:]) - 1
                    if row3 != row1 or row3 != col1 or  col3 != col1 or col3 != row1 and row3 != row2 or row3 != col2 or col3 != col2 or col3 != col2:
                        playerDisplayGrid[row3][col3] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
                        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)  
                        # asks and defines orientation for 2x1 ship
                        orientation = input(f"Choose your ship orientation for {playerShip2_name} (v for vertical, h for horizontal)").strip()
                        while True:
                            if orientation.lower() != "h" and orientation.lower() != "v" :
                                os.system('cls' if os.name == 'nt' else 'clear')
                                BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
                                orientation = input(f"Choose your ship orientation(v for vertical, h for horizontal)").strip()
                            else:
                                break
                        while True:
                            if orientation.lower()=="v":
                                if row3 < row_list-1:
                                    row4 = row3 + 1
                                    col4 = col3 
                                    break
                                else:
                                    row4 = row3 - 1
                                    col4 = col3
                                    break
                            else:
                                break
                        while True:      
                            if orientation.lower()=="h":
                                if col3 < col_list-1:
                                    row4 = row3
                                    col4 = col3 + 1
                                    break
                                else:
                                    row4 = row3
                                    col4 = col3 - 1
                                    break
                            else:
                                break
                                                                
                        break
                else:
                    print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")
            break
        
        # generates coords of the player ship 2x1

        playerDisplayGrid[row3][col3] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)
        
        playerDisplayGrid[row4][col4] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
        BattleGrid(turn, computerDisplayGrid, playerDisplayGrid, row_list, col_list)

        while True:
                satisfied = input(f"Is this where you want {playerShip2_name}? (Y/N) ").strip()
                if satisfied.lower() == "y":
                    break
                elif satisfied.lower() != "n":
                    print(f"Invalid input. Please enter Y or N: ")
                else:
                    playerDisplayGrid[row3][col3] = " "
                    playerDisplayGrid[row4][col4] = " "
                    playerCoordGrid[row3][col3] = " "
                    playerCoordGrid[row4][col4] = " "

                    break

        if satisfied.lower() == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    
    playerShips.update({playerShip2_name: [f"First Coord: ({row3}, {col3})   Second Coord: ({row4}, {col4})"]}) # Adds Ship Name And Coords To Dict


#///////////////////////////////////////////////////////////////////////////(Inputs For Computer Ship Placement)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#   
    # Initialize ship positions for computer randomly
    orientation = ["v","h"]
    computerShips = {}

    while True: # Computer Ship 1 Name 
        computerShip1_name = input("Name the computer's first ship: ")
        if computerShip1_name == playerShip1_name or computerShip1_name == playerShip2_name:
            print("That's already the name of one of your ships. Please name the computer's first ship differently.")
        else:
            break
    
    while True: # Computer Ship 2 Name 
        computerShip2_name = input("Name the computer's second ship: ")
        if computerShip1_name == playerShip1_name or computerShip1_name == playerShip2_name:
            print("That's already the name of one of your ships. Please name the computer's second ship differently.")
        elif computerShip2_name == computerShip1_name:
            print("That's already the name of the computer's first ship. Please name its second ship differently.")
        else:
            break

    random1_StartRowCoord = random.randint(0, row_list - 1) # Computer Ship 1 Starting Row
    random1_StartColCoord = random.randint(0, col_list - 1) # Computer Ship 1 Starting Col
    
    random2_StartRowCoord = random.randint(0, row_list - 1) # Computer Ship 2 Starting Row
    random2_StartColCoord = random.randint(0, col_list - 1) # Computer Ship 2 Starting Col

    # asks and defines orientation for 2x1 ship
    randomOrientation1 = random.choice(orientation)
    randomOrientation2 = random.choice(orientation)

    
    while True: # Computer Ship 1 Orientation Logic Vertical
        if randomOrientation1=="v":
            if random1_StartRowCoord < row_list-1:
                attachedShip1Row = random1_StartRowCoord + 1
                attachedShip1Col = random1_StartColCoord 
                break
            else:
                attachedShip1Row = random1_StartRowCoord - 1
                attachedShip1Col = random1_StartColCoord
                break
        else:
            break
    while True: # Computer Ship 1 Orientation Logic Horizontal     
        if randomOrientation1=="h":
            if random2_StartColCoord < col_list-1:
                attachedShip1Row = random1_StartRowCoord
                attachedShip1Col = random1_StartColCoord + 1
                break
            else:
                attachedShip1Row = random1_StartRowCoord
                attachedShip1Col = random1_StartColCoord - 1
                break
        else:
            break

    while True: # Computer Ship 2 Orientation Logic Vertical
        if randomOrientation2=="v":
            if random2_StartRowCoord < row_list-1:
                attachedShip2Row = random2_StartRowCoord + 1
                attachedShip2Col = random2_StartColCoord 
                break
            else:
                attachedShip2Row = random2_StartRowCoord - 1
                attachedShip2Col = random2_StartColCoord
                break
        else:
            break
    while True: # Computer Ship 2 Orientation Logic Horizontal   
        if randomOrientation2=="h":
            if random2_StartColCoord < col_list-1:
                attachedShip2Row = random2_StartRowCoord
                attachedShip2Col = random2_StartColCoord + 1
                break
            else:
                attachedShip2Row = random2_StartRowCoord
                attachedShip2Col = random2_StartColCoord - 1
                break
        else:
            break


    

    while True:
        if random1_StartRowCoord != random2_StartRowCoord and random1_StartColCoord != random2_StartColCoord: # Ensures Comp Ship 1 & 2 Dont Contain Same Starting Coord
            break
        else:
            random2_StartRowCoord = random.randint(0, row_list - 1)
            random2_StartColCoord = random.randint(0, col_list - 1)
    
    computerShips.update({computerShip1_name: [f"First Coord: ({random1_StartRowCoord}, {random1_StartColCoord})    Second Coord: ({attachedShip1Row},{attachedShip1Col})"]}) # Updates Ship Dict
    computerShips.update({computerShip2_name: [f"First Coord: ({random2_StartRowCoord}, {random2_StartColCoord})    Second Coord: ({attachedShip2Row},{attachedShip2Col})"]}) # Updates Ship Dict


    # Alternates turns between the computer and the player
    while True:
        #Comp Turn
        Turn_system(0, playerShips, computerShips, playerDisplayGrid, playerCoordGrid, playerShip1_name, playerShip2_name, computerShip1_name, computerShip2_name, computerDisplayGrid, computerCoordGrid, row1, col1, row2, col2, row3, col3, row4, col4, random1_StartRowCoord, random1_StartColCoord, random2_StartRowCoord, random2_StartColCoord, attachedShip1Row, attachedShip1Col, attachedShip2Row, attachedShip2Col, row_list, col_list)  
        #Player Turn
        Turn_system(1, playerShips, computerShips, playerDisplayGrid, playerCoordGrid, playerShip1_name, playerShip2_name, computerShip1_name, computerShip2_name, computerDisplayGrid, computerCoordGrid, row1, col1, row2, col2, row3, col3, row4, col4, random1_StartRowCoord, random1_StartColCoord, random2_StartRowCoord, random2_StartColCoord, attachedShip1Row, attachedShip1Col, attachedShip2Row, attachedShip2Col, row_list, col_list)  
        
        
        
#///////////////////////////////////////////////////////////////////////////(Calling The Game() Funtion)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#        
# Entire functioning program: 206 lines
# (Lines w/out animations)        
main()

