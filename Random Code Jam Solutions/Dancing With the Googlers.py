def dancing_googlers(filename):
    file = open(filename)
    out = open("output.txt", 'w+')
    testcases = int(file.readline())
    for test in range(0, testcases):
        temp = file.readline().split(' ')
        N = int(temp.pop(0))
        S = int(temp.pop(1))
        p = int(temp.pop(2))
        count = 0
        surprise = 0
        for score in range(0, len(temp)):
            for i in range(0,11):
                for j in range(0,11):
                    for k in range(0,11):
                        if abs(i-j) < 3 and abs(j-k) < 3 and abs(i-k) < 3:
                            if abs(i-j) == 2 or abs(j-k) == 2 or abs(i-k) == 2:
                                surprise += 1
                                if surprise > S:
                                    break
                                if (i+j+k == int(temp[score])):
                                    if i >= p or j >= p or k >= p:
                                        count += 1

        print("Case #" + str(test+1) + ": " + str(count) + '\n')
