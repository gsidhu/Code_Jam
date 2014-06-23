def professor_normal(filename):
    import math
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for i in range(0, testcases):
        game = []
        M = int(file.readline())
        N = int(file.readline())
        for j in range(0, M):
            game.append(file.readline().strip("\n").split(" "))
        if 
