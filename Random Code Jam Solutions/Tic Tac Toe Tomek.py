                            ## TIC TAC TOE TOMEK START ##

def straight(game):
    for j in game:
        if j.count('T') == 1:
            if j.count('X') == 3:
                print ('X won.')
                return True
            elif j.count('O') == 3:
                print('O won.')
                return True
            else:
                return False
        elif j.count('X') == 4:
            print('X won.')
            return True
        elif j.count('O') == 4:
            print('O won.')
            return True
        
def simplegame(game, game_col, game_diagonal):
    game_col = []
    game_diagonal = []
    ## straight row
    if straight(game) == True:
        return True
    else:      
        ## straight column
        for k in range(0, 4):
            game_col.append(game[0][k] + game[1][k] + game[2][k] + game[3][k])
        if straight(game_col) == True:
            return True
        else:
            ## diagonal
            game_diagonal.append(game[0][0] + game[1][1] + game[2][2] + game[3][3])
            game_diagonal.append(game[0][3] + game[1][2] + game[2][1] + game[3][0])
            if straight(game_diagonal) == True:
                return True
            else:
                return False
    return False

def tictac(filename):
    file = open(filename, 'r')
    ## number of test cases
    num_cases = int(file.readline())
    var = 0
    while var < num_cases:
        game = []
        game_col = []
        game_diagonal = []
        for i in range(0,5):
            ## 1 game in array. every element is a subsequent row.
            game.append(file.readline().strip('\n'))

        ## simple game
        if simplegame(game, game_col, game_diagonal) == False:        
            ## draw game
            draw_text = ''.join(sorted(''.join(set(''.join(game)))))
            if draw_text ==  'OTX' or draw_text == 'OX':
                print ("Draw")
                game = []
                game_col = []
                game_diagonal = []
                var += 1
                continue
            ## in progress
            else:
                print ("Game has not completed")
                game = []
                game_col = []
                game_diagonal = []
                var += 1
                continue
        else:
            game = []
            game_col = []
            game_diagonal = []    
            var += 1
            continue
        
                            ## TIC TAC TOE TOMEK END ##
