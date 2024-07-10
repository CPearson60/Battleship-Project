def computer_win():


    print(f"   ___                            _              __    __ _           ")
    print(f"  / __\___  _ __ ___  _ __  _   _| |_ ___ _ __  / / /\ \ (_)_ __  ___ ")
    print(f" / /  / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| \ \/  \/ / | '_ \/ __|")
    print(f"/ /__| (_) | | | | | | |_) | |_| | ||  __/ |     \  /\  /| | | | \__ \ ") 
    print(f"\____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \/  \/ |_|_| |_|___/")
    print(f"                     |_|                                              ")

    print("                            .-=========-.")
    print("                            \'-=======-'/")
    print("                            _|   .=.   |_")
    print("                           ((|  {{1}}  |))")
    print("                            \|   /|\   |/")
    print("                             \__ '`' __/")
    print("                               _`) (`_" )
    print("                             _/_______\_")
    print("                            /___________\ ")


def player_win():
    print("   ___ _                          __    __ _           ")
    print("  / _ \ | __ _ _   _  ___ _ __   / / /\ \ (_)_ __  ___ ")
    print(" / /_)/ |/ _` | | | |/ _ \ '__|  \ \/  \/ / | '_ \/ __|")
    print("/ ___/| | (_| | |_| |  __/ |      \  /\  /| | | | \__ \ ")
    print("\/    |_|\__,_|\__, |\___|_|       \/  \/ |_|_| |_|___/")
    print("               |___/                                  ")
    
    
    print("                      .-=========-.")
    print("                      \'-=======-'/")
    print("                       |   .=.   |_")
    print("                     ((|  {{1}}  |))")
    print("                      \|   /|\   |/")
    print("                       \__ '`' __/")
    print("                         _`) (`_" )
    print("                       _/_______\_")
    print("                      /___________\ ")
    
player_win()


print(f"""{Fore.RED}Description:
{Fore.LIGHTBLACK_EX}    The game starts with a 5x5 grid displayed on the screen.
{Fore.LIGHTBLACK_EX}    You will be prompted to input the coordinates where you want to shoot.
{Fore.LIGHTBLACK_EX}    Coordinates should be in the format X,# (e.g., A,1).
{Fore.LIGHTBLACK_EX}    If your shot hits the ship, you win and the game ends.
{Fore.LIGHTBLACK_EX}    If your shot misses, you can try again.
{Fore.LIGHTBLACK_EX}    The game will update the grid after each shot to reflect the shots fired.\n""")

print(Fore.WHITE+"Create Your Grid:")
col_list = int(input(Fore.BLUE+"    How many columns (max 26): "))
while col_list >= 27:
    col_list = int(input("  Too many. Maximum columns is 26. How many columns: "))

row_list = int(input("  How many rows (max 26): "))
while row_list >= 27:
    row_list = int(input("  Too many. Maximum rows is 26. How many rows: "))