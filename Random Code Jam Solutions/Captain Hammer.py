def captain_hammer(filename):
    import math
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for i in range(0, testcases):
        var = file.readline().split(" ")
        v = int(var[0])
        d = int(var[1])
        theta = ((9.8 * d)/v**2)/2
        ans = math.degrees(math.asin(theta))
        result = "Case #" + str(i+1) + ": " + str(ans)
        ##print(str(theta) + "\t" + str(ans))
        out.write(result + "\n")
