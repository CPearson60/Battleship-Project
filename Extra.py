import random
import os
from colorama import init, Fore, Style
import time, keyboard

# Initialize Colorama for colored output
init()







####################################################(Animations)############################################################### 
#V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V 


####################################################(Animations - Cameron)############################################################### 
# shipAnimation_miss(), shipAnimation_hit(), computer_win(), player_win() are all just animations put into a function

def shipAnimation_miss():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""                                   
                                        ---
                                        / | [
                                !      | |||
                                _/|     _/|-++'
                            +  +--|    |--|--|_ |-
                        { /|__|  |/\__|  |--- |||__/
                        +---------------___[}-_===_.'____           ___      
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    |                                                                     BB-61/
    \_________________________________________________________________________|""")
    time.sleep(.2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(""""                                   
                                        ---
                                        / | [
                                !      | |||
                                _/|     _/|-++'
                            +  +--|    |--|--|_ |-
                        { /|__|  |/\__|  |--- |||__/                  __
                        +---------------___[}-_===_.'____           __/ /     
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    |                                                                     BB-61/
    \_________________________________________________________________________|""")
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(""""                                   
                                        ---                            
                                        / | [                         /\ 
                                !      | |||                          ||
                                _/|     _/|-++'                       ||
                            +  +--|    |--|--|_ |-                    ** 
                        { /|__|  |/\__|  |--- |||__/                  **
                        +---------------___[}-_===_.'____           __| |     
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    |                                                                     BB-61/
    \_________________________________________________________________________|""")
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""                                                    
                                                                      **
                                                                   ********
                                        ---                      ************
                                        / | [                      ******* 
                                !      | |||                          **
                                _/|     _/|-++'                        
                            +  +--|    |--|--|_ |-                      
                        { /|__|  |/\__|  |--- |||__/                  
                        +---------------___[}-_===_.'____           __| |     
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    """)
   
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("           _      ")   
    print(" _ __ ___ (_)___ ___ ")
    print("| '_ ` _ \| / __/ __|")
    print("| | | | | | \__ \__ \ ")
    print("|_| |_| |_|_|___/___/")    
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    

####################################################(Animations)############################################################### 
def shipAnimation_hit():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""                                   
                                        ---
                                        / | [
                                !      | |||
                                _/|     _/|-++'
                            +  +--|    |--|--|_ |-
                        { /|__|  |/\__|  |--- |||__/
                        +---------------___[}-_===_.'____           ___      
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    |                                                                     BB-61/
    \_________________________________________________________________________|""")
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(""""                                   
                                        ---
                                        / | [
                                !      | |||
                                _/|     _/|-++'
                            +  +--|    |--|--|_ |-
                        { /|__|  |/\__|  |--- |||__/                  __
                        +---------------___[}-_===_.'____           __/ /     
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    |                                                                     BB-61/
    \_________________________________________________________________________|""")
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(""""                                   
                                        ---                            
                                        / | [                         /\ 
                                !      | |||                         ||
                                _/|     _/|-++'                        ||
                            +  +--|    |--|--|_ |-                     ** 
                        { /|__|  |/\__|  |--- |||__/                  **
                        +---------------___[}-_===_.'____           __| |     
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    |                                                                     BB-61/
    \_________________________________________________________________________|""")
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""                                                                  /\ 
                                                                    || 
                                        ---                           || 
                                        / | [                         ** 
                                !      | |||                         **
                                _/|     _/|-++'                        
                            +  +--|    |--|--|_ |-                      
                        { /|__|  |/\__|  |--- |||__/                  
                        +---------------___[}-_===_.'____           __| |     
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___/     _
    __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
    """)
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
                        _____
                    ____/     \_____                                   /\ 
                __/    \________   \                                  ||
                /                \   \                                 ||
                |________________|____\                                **
                                        ---                           ** 
                                        / | [                          
                                !      | |||                         
                                _/|     _/|-++'                        
                            +  +--|    |--|--|_ |-                     
                        { /|__|  |/\__|  |--- |||__/                     
    """)
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
                                                                    /\ 
                                                                    ||      
                                                                    ||
                        _____                                         **
                    ____/     \_____                                   ** 
                __/    \________   \                                  
                /                \   \                                 
                |________________|____\                                
                                        ---                            
                                        / | [                          
                                !      | |||                                                                           
    """)
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
                                                                    /\      
                                                                    ||      
                                                                    ||      
                                                                    **
                                                                    **

                        _____                                         
                    ____/     \_____                                    
                __/    \________   \                                                                                                 
    """)

    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
        
        
                                                                    /\      
                                                                    ||      
                                                                    ||      
                                                                    **
                                                                    **
                                                                                                                                
    """)

    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
        
        
        
        
        
                                                                    /\      
                                                                    ||      
                                                                    ||      
                                                                    **                                                                                              
    """)

    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
        
        
        
        
        


                                                                                                            
    """)



    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
        
        
        
        
        
                                                                    **
                                                                    **                                                                                                       
    """)


    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
        

                                                                    **
                                                                    **   
                                                                    ||
                                                                    ||
                                                                    \/
                                                                    
                                                                                                                                                                        
    """)

    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
                                                                    **
                                                                    **   
                                                                    ||
                                                                    ||
                                                                    \/
                                                                    
                                                                
                                                                                            
                                                    ---
                                                    / | [
                                            !      | |||
                                            _/|     _/|-++'
                                        +  +--|    |--|--|_ |-                                                                                                                                                                       
    """)

    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
    
                                                                    
                                                                    **
                                                    ---                **
                                                    / | [              ||
                                            !      | |||               ||
                                            _/|     _/|-++'            \/
                                        +  +--|    |--|--|_ |-         
                                    { /|__|  |/\__|  |--- |||__/
                                    +---------------___[}-_===_.'____           ___      
                                ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _                                                                                                                                                               
    """)


    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
                
                                                    ---
                                                    / | [
                                            !      | |||                **
                                            _/|     _/|-++'             **
                                        +  +--|    |--|--|_ |-          ||
                                    { /|__|  |/\__|  |--- |||__/        ||
                                    +---------------___[}-_===_.'____   \/      ___      
                                ____`-' ||___-{]_| _[}-  |     |_[___\==--     /___===      _
                __..._____--==/___]_|__|_____________________________[___\==--|___|,------' .7
                |                                                                     BB-61/
                \_________________________________________________________________________|                                                                                                                                                             
    """)

    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
                                    
                                    
                                
                                
                
                                

                                            .-=||  | |=-.   
                                            `-=#$%&%$#=-'   
                                                | ;  :|     
                                        _____.,-#%&$@%#&#~,._____                                                                                                                                                       
    """)



    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
        
        
                                        _.-^^---....,,--       
                                    _--                  --_  
                                    \._                   _./  
                                        ```--. . , ; .--'''       
                                            | |   |             
                                        .-=||  | |=-.   
                                        `-=#$%&%$#=-'   
                                            | ;  :|     
                                    _____.,-#%&$@%#&#~,._____                                                                                                                                           
    """)



    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""""
                                        _.-^^---....,,--       
                                    _--                  --_  
                                    <                        >)
                                    |                         | 
                                    \._                   _./  
                                        ```--. . , ; .--'''       
                                            | |   |             
                                        .-=||  | |=-.   
                                        `-=#$%&%$#=-'   
                                            | ;  :|     
                                    _____.,-#%&$@%#&#~,._____                                                                                                                           
    """)


    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" _     _ _   ")   
    print("| |__ (_) |_ ")
    print("| '_ \| | __|")
    print("| | | | | |_  ")
    print("|_| |_|_|\__|")      

    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")   
    print("")
    print("")
    print("")
    print("")      
    time.sleep(.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" _     _ _   ")   
    print("| |__ (_) |_ ")
    print("| '_ \| | __|")
    print("| | | | | |_  ")
    print("|_| |_|_|\__|")      
    time.sleep(.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")   
    print("")
    print("")
    print("")
    print("")      
    time.sleep(.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" _     _ _   ")   
    print("| |__ (_) |_ ")
    print("| '_ \| | __|")
    print("| | | | | |_  ")
    print("|_| |_|_|\__|")      
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    

####################################################(Animations)############################################################### 
def computer_win():


    print(Fore.BLUE + f"   ___                            _              __    __ _           ")
    print(Fore.BLUE + f"  / __\___  _ __ ___  _ __  _   _| |_ ___ _ __  / / /\ \ (_)_ __  ___ ")
    print(Fore.BLUE + f" / /  / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| \ \/  \/ / | '_ \/ __|")
    print(Fore.BLUE + f"/ /__| (_) | | | | | | |_) | |_| | ||  __/ |     \  /\  /| | | | \__ \ ") 
    print(Fore.BLUE + f"\____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \/  \/ |_|_| |_|___/")
    print(Fore.BLUE + f"                     |_|                                              ")

    print(Fore.YELLOW+"                            .-=========-.")
    print(Fore.YELLOW+"                            \'-=======-'/")
    print(Fore.YELLOW+"                            _|   .=.   |_")
    print(Fore.YELLOW+"                           ((|  {{1}}  |))")
    print(Fore.YELLOW+"                            \|   /|\   |/")
    print(Fore.YELLOW+"                             \__ '`' __/")
    print(Fore.YELLOW+"                               _`) (`_" )
    print(Fore.YELLOW+"                             _/_______\_")
    print(Fore.YELLOW+"                            /___________\ \n")

####################################################(Animations)###############################################################  
def player_win():
    print(Fore.BLUE + "   ___ _                          __    __ _           ")
    print(Fore.BLUE + "  / _ \ | __ _ _   _  ___ _ __   / / /\ \ (_)_ __  ___ ")
    print(Fore.BLUE + " / /_)/ |/ _` | | | |/ _ \ '__|  \ \/  \/ / | '_ \/ __|")
    print(Fore.BLUE + "/ ___/| | (_| | |_| |  __/ |      \  /\  /| | | | \__ \ ")
    print(Fore.BLUE + "\/    |_|\__,_|\__, |\___|_|       \/  \/ |_|_| |_|___/")
    print(Fore.BLUE + "               |___/                                  ")
    
    
    print(Fore.YELLOW+"                      .-=========-.")
    print(Fore.YELLOW+"                      \'-=======-'/")
    print(Fore.YELLOW+"                       |   .=.   |_")
    print(Fore.YELLOW+"                     ((|  {{1}}  |))")
    print(Fore.YELLOW+"                      \|   /|\   |/")
    print(Fore.YELLOW+"                       \__ '`' __/")
    print(Fore.YELLOW+"                         _`) (`_" )
    print(Fore.YELLOW+"                       _/_______\_")
    print(Fore.YELLOW+"                      /___________\ \n")


####################################################(End Of Animations)############################################################### 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
####################################################(Actual Code | Functions)###############################################################  

#V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V V  
 
 
 
 
 
 
 
 
 
# Gianna
#int_input() function accounts for edge cases and used to force quit game
def int_input(prompt, selection):
    x = input(prompt)
    while not x.isnumeric() or not int(x) in selection:
        # repeats prompt until satisfactory input
        if x.lower() == "quit":
            # force quits if the user inputs "quit"
            print("The game has been forced quit. Have a nice day!")
            quit()
        else:
            x = input(prompt)
    return int(x)
    
    
# Cameron
# battleGrid() function to create and display the battle grid
def battleGrid(displayGrid,row_list,col_list):
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
        for j in range(col_list):
            print(displayGrid[i][j], end="   | ")  # Print grid content
        print()
        
        
        
    
# Cameron
# Function for player to shoot
def player_shoot(displayGrid,coordGrid,col_list,row_list):
    while True:
        shot = input(Fore.RED + f"Where do you want to shoot (A-{chr(65 + row_list - 1)},1-{col_list})? ").strip().replace(",", "")
        # .lower is case insinstive 
        if shot.lower() == "quit":
            print("The game has been forced quit. Have a nice day!")
            quit()
        #ensures length of character is atleast 2 | checks if first character is valid and within range | ensures character is digit *valid column number coverts & into int
        elif len(shot) >= 2 and shot[0].upper() in [chr(65 + i) for i in range(row_list)] and shot[1:].isdigit() and int(shot[1:]) <= col_list:
            break
        else:
            print(Fore.RED + f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

    # generate shot coordinates
    # the fuction ord generates unicode for input
    # converts into a numberic number
    #example: ord('B') - ord('A') gives 66 - 65 = 1
    row = ord(shot[0].upper()) - ord('A')
    
    #shot[1] = int value | number value
    col = int(shot[1:]) - 1
    while True:
        if coordGrid[row][col] == 'x':
            while True:
                print("Point Was Already Shot!!")
                shot = input(Fore.RED + f"Where do you want to shoot (A-{chr(65 + row_list - 1)},1-{col_list})? ").strip().replace(",", "")
                # .lower is case insinstive 
                if shot.lower() == "quit":
                    print("The game has been forced quit. Have a nice day!")
                    quit()
                #ensures length of character is atleast 2 | checks if first character is valid and within range | ensures character is digit *valid column number coverts & into int
                elif len(shot) >= 2 and shot[0].upper() in [chr(65 + i) for i in range(row_list)] and shot[1:].isdigit() and int(shot[1:]) <= col_list:
                    row = ord(shot[0].upper()) - ord('A')
                    col = int(shot[1:]) - 1                  
                    break
                else:
                    print(Fore.RED + f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")     
        else:
            break   
           
    X = "x"
    displayGrid[row][col] = f"{Fore.LIGHTYELLOW_EX}{X}{Fore.BLUE}"
    coordGrid[row][col] = X
    return (displayGrid, coordGrid, X)

# Gianna
def computer_shoot(row_list,col_list,displayGrid,coordGrid):
    random_num1 = random.randint(0, row_list - 1)
    random_num2 = random.randint(0, col_list - 1)
    
    while True: 
        row = random_num1
        col = random_num2
        if coordGrid[row][col] == 'x':
            random_num1 = random.randint(0, row_list - 1)
            random_num2 = random.randint(0, col_list - 1)
        else:
            break

    print(f"Computer shoots at {random_num1},{random_num2}")

    X = "x"
    displayGrid[row][col] = f"{Fore.LIGHTMAGENTA_EX}{X}{Fore.BLUE}"
    coordGrid[row][col] = X
    return (displayGrid, coordGrid, X)


# Gianna
# Function for computer to place ships
def user_turn(displayGrid,coordGrid,random_num3,random_num4,row_list,col_list):
    
    print(Fore.RED + "User Objective:\nSink The Computer's Ship In Five Turns")
    
    battleGrid(displayGrid,row_list,col_list)
    player_shoot(displayGrid,coordGrid,col_list,row_list)
    if coordGrid[random_num3][random_num4] != "x":
        shipAnimation_miss()

    # Check if player hits ship 1 or ship 2
    if coordGrid[random_num3][random_num4] == "x":
        shipAnimation_hit()
        print("You sunk the Computer's ship! You WIN!")
        player_win()
        t=10
        while t > 0:
            print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
            time.sleep(1)  # wait for 1 second
            t -= 1
        game(gridCreate_check,row_list,col_list)
        
        
        
    os.system('cls' if os.name == 'nt' else 'clear')
    

# Gianna
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
        t=10
        while t > 0:
            print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
            time.sleep(1)  # wait for 1 second
            t -= 1
        game(gridCreate_check,row_list,col_list)

    os.system('cls' if os.name == 'nt' else 'clear')

# Cameron
# Welcome message and grid size input
def game(gridCreate_check,row_list,col_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.WHITE +"Welcome to Battleship!")


    print(Fore.RED +   " ______           _     _   __                __        _                                                         ___#_#___|__")                                          
    print(Fore.RED +   "|_   _ \         / |_  / |_[  |              [  |      (_)                                                    _  |____________|  _")                             
    print(Fore.RED +   "  | |_) |  ,--. `| |-'`| |-'| | .---.  .--.   | |--.   __  _ .--.                                    =====| |.---------------------------. | |====")                            
    print(Fore.WHITE + "  |  __'. `'_\ : | |   | |  | |/ /_\_\( (`\]  | .-. | [  |[ '/'`\ \                <--------------------'   .  .  .  .  .  .  .  .   '--------------/")                        
    print(Fore.WHITE + " _| |__) |// | |,| |,  | |, | || \__., `'.'.  | | | |  | | | \__/ |                 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")                   
    print(Fore.BLUE +  "|_______/ \-;__/\__/  \__/[___]'.__.'[\__) )[___]|__][___] | ;.___/                |                                                                     BB-61/")               
    print(Fore.BLUE +  "                                                           [__|                    \_______________________________________________WWS______________________/")


    print(f"""{Fore.RED}Description:
    {Fore.LIGHTBLACK_EX}    The game starts with a grid of your choosing displayed on the screen.
        You will be prompted to input the coordinates where you want to shoot.
        Coordinates should be in the format X,# (e.g., A,1).
        If your shot hits the ship, you win and the game ends.
        If your shot misses, you can try again.
        The game will update the grid after each shot to reflect the shots fired.
    {Fore.RED}    Please enter \"Quit\" at any time during the game to end the game.\n""")


    print (f"""
{Fore.RED}Menu Selection:     
    
{Fore.BLUE}       [1] Select Grid
    
{Fore.BLUE}       [2] Start Single Player  
    
{Fore.BLUE}       [3] Quit Game               
                    
                           """)


    
    while True:
        
        if keyboard.read_key() == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.WHITE+"Create Your Grid:")
            while True:
                
                col_list = int_input(Fore.BLUE+"    How many columns (max 26): ", range(0, 27))

                row_list = int_input("    How many rows (max 26): ", range(0, 27))
                
                displayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)] 
                
                battleGrid(displayGrid,row_list,col_list)
                
                
                while True: 
                    print("Are You Satsified With Your Board:\n   [1]Yes\n   [2]Create New Board\n")
                    if keyboard.read_key() == '1':
                        gridCreate_check=1       
                        game(gridCreate_check,row_list,col_list)
                        break
                        
                    if keyboard.read_key() == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        col_list = int_input(Fore.BLUE+"    How many columns (max 26): ", range(0, 27))

                        row_list = int_input("    How many rows (max 26): ", range(0, 27))
                        
                        displayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)] 
                        
        elif keyboard.read_key() == '3':
            print("\nThe game has been forced quit. Have a nice day!")
            quit()
            
        else:
            if keyboard.read_key() == '2' and gridCreate_check == 1:
                
                # Gianna
                # Initialize grids
                displayGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]
                coordGrid = [[" " for _ in range(col_list)] for _ in range(row_list)]

                print (Fore.RED + "Ship Placement Single Player Selection:\n")
                # Display initial ship placement grid
                battleGrid(displayGrid,row_list,col_list)
                # Input for user ship
                while True:
                    ship1 = input(f"\nPlease enter the coordinate for your ship (A-{chr(65 + row_list - 1)},1-{col_list}): ").strip().replace(",", "")
                    if ship1.lower() == "quit":
                        print("\nThe game has been forced quit. Have a nice day!")
                        quit()
                    elif len(ship1) >= 2 and ship1[0].upper() in [chr(65 + i) for i in range(row_list)] and ship1[1:].isdigit() and int(ship1[1:]) <= col_list:
                        break
                    else:
                        print(f"\nInvalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")

                # generates coords of the user ship
                row1 = ord(ship1[0].upper()) - ord('A')
                col1 = int(ship1[1:]) - 1

                # Initialize ship positions for computer randomly
                random_num3 = random.randint(0, row_list - 1)
                random_num4 = random.randint(0, col_list - 1)
                while True:
                    if random_num3 != row1 and random_num4 != col1:
                        break
                    else:
                        random_num3 = random.randint(0, row_list - 1)
                        random_num4 = random.randint(0, col_list - 1)

                # Mark ship on shipPlaceGrid
                displayGrid[row1][col1] = f"{Fore.LIGHTRED_EX}O{Fore.BLUE}"
                battleGrid(displayGrid,row_list,col_list)

                # Alternates turns between the computer and the player
                while True:
                    computer_turn(displayGrid, coordGrid,row1,col1,row_list,col_list)
                    user_turn(displayGrid,coordGrid,random_num3,random_num4,row_list,col_list)
            elif keyboard.read_key(1) == '2' and gridCreate_check != 1:
                
                print("Create grid first")

gridCreate_check=0  
row_list = 0
col_list = 0
game(gridCreate_check,row_list,col_list)

# Entire functioning program: 206 lines
# (Lines w/out animations)

# Cameron - Current state of the game