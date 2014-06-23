import random

def good(init, N):
    for i in range(0, N):
        p = random.choice(range(i,N))
        var = init[i]
        init[i] = init[p]
        init[p] = var
    return init

def bad(init, N):
    for i in range(0, N):
        p = random.choice(range(0,N))
        var = init[i]
        init[i] = init[p]
        init[p] = var
    return init

def swap(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):
        N = int(file.readline())
        init = []
        copy = []
        badder = 0
        
        for i in range(0, N):
            init.append(str(i))
##            g1.append(i)
##            b1.append(i)
##        count = 1000
##        while count > 0:
##            g1 = good(init, N)
##            b1 = bad(init, N)
##            tg.append(g1)
##            tb.append(b1)
##            count -= 1

        given = file.readline().strip('\n').split(' ')
##        for i in range(0, N):
##            copy.append(given[i])
        for i in range(0, N):
            if given.count(given[i]) > 1 or init == given:
                badder = 1
        
        if badder == 1:
            print("Case #" + str(test+1) + ": BAD\n")
        elif badder == 0:
            print("Case #" + str(test+1) + ": GOOD\n")
