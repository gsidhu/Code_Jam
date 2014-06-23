def rotate(filename):
    file = open(filename)
    testcases = int(file.readline())
    output = open('output.txt', 'w')
    for test in range(1, testcases+1):
        N, K = file.readline().split(' ')
        N = int(N)
        K = int(K.strip('\\n'))
        game = []
        for count in range(0, N):
            row = list(file.readline())
            game.append(row)
##        for i in game:
##            print('  '.join(i))
##        print('-------------')
## gravity play     
        magic = N
        while magic > 0:
            for i in range(0, N):
                for j in range(0, N-1):
                    if game[i][j] == 'B' or game[i][j] == 'R':
                        if game[i][j+1] == '.':                    
                            game[i][j+1] = game[i][j]
                            game[i][j] = '.'
            magic -= 1
##        for i in game:
##            print('  '.join(i))
##        print('-'*N)            
## check
        B = 'B'*K
        R = 'R'*K
        rob = 0
        bro = 0
        row = []
        column = []
        diagonal1 = []
        diagonal2 = []
        for i in range(0, N):
            var1 = ''
            var2 = ''
            diagonal1.append('')
            diagonal1.append('')
            diagonal2.append('')
            diagonal2.append('')
            for j in range(0, N):
                var1 += game[i][j]
                var2 += game[j][i]
            row.append(var1)
            column.append(var2)
        for i in range(0, N):
            for j in range(0, N):
                diagonal1[i+j] += game[i][j]
        for bob in game:
            bob.pop(-1)
            bob.reverse()
            bob.append('\n')
        for i in range(0, N):
            for j in range(0, N):
                diagonal2[i+j] += game[i][j]
        for r in row:
            for c in column:
                for d1 in diagonal1:
                    for d2 in diagonal2:
                        if R in r or R in c or R in d1 or R in d2:
                            rob = 1
                        if B in r or B in c or B in d1 or B in d2:
                            bro = 1
        if rob == 1 and bro == 1:
            output.write('\nCase #' + str(test) + ": Both")
        elif rob == 0 and bro == 0:
            output.write('\nCase #' + str(test) + ": Neither")
        elif rob == 0 and bro == 1:
            output.write('\nCase #' + str(test) + ": Blue")
        elif rob == 1 and bro == 0:
            output.write('\nCase #' + str(test) + ": Red")
        print(str(test))
##        for i in game:
##            print('  '.join(i))
##        print('-'*N)            
    file.close()
    output.close()
