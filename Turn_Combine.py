

def Turn_system(turn,playerDisplayGrid, playerCoordGrid, ship1_name, ship2_name, computerDisplayGrid, computerCoordGrid, row1, col1, row2, col2, row3, col3, row4, col4, random_num3, random_num4, row_list, col_list):
    print("Objective:\nSink The Computer's Ship")
    if turn == 0:
        playerBattleGrid(playerDisplayGrid, row_list, col_list)
        turn=0
        Shoot_Guess(playerDisplayGrid, playerCoordGrid,row_list, col_list,turn)

        if playerCoordGrid[row1][col1] == playerCoordGrid[row2][col2] == playerCoordGrid[row3][col3] == playerCoordGrid[row4][col4] == "x":
            print("The computer sunk both your ships! Better luck next time.")
            computer_win()
        t=5
        while t > 0:
            print(f"{Fore.WHITE}Player moves in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
            time.sleep(1)  # wait for 1 second
            t -= 1
            
    
        # Check if player hits ship 1 or ship 2
        print("Move Log:")
        if playerCoordGrid[row1][col1] == "x":
            print(f"The computer hit your ship, {ship1_name}!")
        if playerCoordGrid[row2][col2] == "x":
            print(f"The computer hit your ship, {ship1_name}!")
        if playerCoordGrid[row3][col3] == "x":
            print(f"The computer hit your ship, {ship2_name}!")
        if playerCoordGrid[row4][col4] == "x":
            print(f"The computer hit your ship, {ship2_name}!")

        if playerCoordGrid[row1][col1] == playerCoordGrid[row2][col2] == "x":
            print(f"The computer sunk your ship, {ship1_name}!")
        if playerCoordGrid[row3][col3] == playerCoordGrid[row4][col4] == "x":
            print(f"The computer sunk your ship, {ship2_name}!")
        else:
            print("The computer missed!")
        t = 3
        print(f"{Fore.WHITE}User turn in{t % 60:02}", end=" seconds.\r")  # display minutes and seconds
        time.sleep(1)  # wait for 1 second


        os.system('cls' if os.name == 'nt' else 'clear')
    
    else:
        computerBattleGrid(computerDisplayGrid, row_list, col_list)
        turn = 1
        Shoot_Guess(computerDisplayGrid, computerCoordGrid, col_list, row_list,turn)
        if computerCoordGrid[random_num3][random_num4] != "x":
            shipAnimation_miss()

        # Check if player hits ship 1 or ship 2
        if computerCoordGrid[random_num3][random_num4] == "x":
            shipAnimation_hit()
            print("You sunk the Computer's ship! You WIN!")
            player_win()
            t=10
            while t > 0:
                print(f"{Fore.WHITE}Back to menu in {t % 60:02}", end=" seconds.\r")  # display minutes and seconds
                time.sleep(1)  # wait for 1 second
                t -= 1
            game()
            
            
            os.system('cls' if os.name == 'nt' else 'clear')