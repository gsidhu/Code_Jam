def move1(strings, N):
    count = 0
    while len(set(strings)) > 1:
        for i in range(N):
            j = 0
            while j < len(strings[i]):
                if strings[i].count(strings[i][j]) > 1:
                    strings[i] = strings[i][:j] + strings[i][j+1:]
                    count += 1
                j += 1
    return count, strings

def repeater(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):
        N = int(file.readline().strip('\n'))
        strings = []
        for i in range(0, N):
            strings.append(file.readline().strip('\n'))
        temp = []
        



    final = "Case #" + str(test+1) + ": " + str(count) +"\n"
    out.write(final)
