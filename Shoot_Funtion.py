#Cameron's Battleship 2.2
import random

row_list = 10
col_list=10

# #computer shot randomizer
# shot = f" {chr(random.randint(65,(65+row_list) ))}{random.randint(1,10)}"

def Shoot_Guess():
    turn = 0
    while True:
        if turn == 0:
            shot = (f" {chr(random.randint(65, 65 + row_list - 1) )}{random.randint(1,col_list)}").strip().replace(",", "")

        else:
            shot = input(f"Where do you want to shoot (A-{chr(65 + row_list - 1)},1-{col_list})? ").strip().replace(",", "")
            
        # .lower is case insinstive 
        if shot.lower() == "quit":
            print("The game has been forced quit. Have a nice day!")
            quit()
        #ensures length of character is atleast 2 | checks if first character is valid and within range | ensures character is digit *valid column number coverts & into int
        elif len(shot) >= 2 and shot[0].upper() in [chr(65 + i) for i in range(row_list)] and shot[1:].isdigit() and int(shot[1:]) <= col_list:
            break
        else:
            print(f"Invalid input. Please enter a valid coordinate (A-{chr(65 + row_list - 1)},1-{col_list}).")
            print (shot)

    # generate shot coordinates
    #example: ord('B') - ord('A') gives 66 - 65 = 1
    row = ord(shot[0].upper()) - ord('A')
    #shot[1] = int value | number value
    col = int(shot[1:]) - 1

player_shoot()