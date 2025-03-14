
game_board = [[1,2,3],[4,5,6],[7,8,9]]
gameon = True

def print_gameboard():
    for i in game_board:
        print(i, end="\n")

while gameon:
    while True:
        print_gameboard()
        player1_guess = int(input("Player 1, where would you like to go? "))
        print()
        for i in game_board:
            for j in i:
                if j == "X" or j == "O":
                    continue
                elif isinstance(j, int) and j == player1_guess:
                    indx = i.index(j)
                    i[indx] = "X"
                else:
                    pass

    #  while True:
    #     print_gameboard()
    #     player2_guess = int(input("Player 2, where would you like to go? "))
    #     print()
    #     for i in game_board:
    #         for j in i:
    #             if j == "X" or j == "O":
    #                 continue
    #             elif isinstance(j, int) and j == player2_guess:
    #                 indx = i.index(j)
    #                 i[indx] = "O"
    #             else:
    #                 break
                

        
    

       