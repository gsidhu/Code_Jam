def flip(x, n):
    for i in range(0, len(x)):
        if x[i][n] == '0':
            x[i] = x[i][:n] + '1' + x[i][n+1:]
        elif x[i][n] == '1':
            x[i] = x[i][:n] + '0' + x[i][n+1:]
    return x
        
def charging_chaos(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):
        N, L = file.readline().strip('\n').split(' ')
        N = int(N)
        L = int(L)
        init = file.readline().strip('\n').split(' ')
        req = file.readline().strip('\n').split(' ')
        count = 0
        win = 0
        a = set(init)
        b = set(req)
        if a == b:
            win = 1
        
        for i in range(0, L):
            temp = flip(init,i)
            count += 1
            a = set(temp)
            b = set(req)
            if a == b:
                win = 1
        if win == 1:
            final = "Case #" + str(test+1) + ": " + str(count) +"\n"
            out.write(final)
        if win == 0:
            final = "Case #" + str(test+1) + ": NOT POSSIBLE\n"
            out.write(final)
