def moist(filename):
    import math
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for i in range(0, testcases):
        names = []
        count = 0
        M = int(file.readline())
        for j in range(0, M):
            names.append(file.readline().strip('\n'))
        for k in range(0, M-1):
            if names[k] > names[k+1]:
                count+= 1
                var = names[k]
                names[k] = names[k+1]
                names[k+1] = var
        result = ("Case #" + str(i+1) + ": " + str(count))
        out.write(result + "\n")
    file.close()
    out.close()
