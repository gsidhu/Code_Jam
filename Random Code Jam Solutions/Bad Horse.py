def badhorse(filename):
    file = open(filename)
    testcases = int(file.readline())
    for i in range(0, testcases):
        set1 = []
        set2 = []
        M = int(file.readline())
        for j in range(0, M):
            name = file.readline().split(" ")
            set1.append(name[0])
            set2.append(name[1].strip("\n"))
        for l in set1:
            if set1.count(l) > 1:
                set1.remove(l)
        for l in set2:
            if set2.count(l) > 1:
                set2.remove(l)
        for k in range(0, len(set1)):
            if set1[k] in set2:
                set2.pop(set2.index(set1[k]))
        if len(set1) > 0 and len(set2) > 0:
            print("Case #" + str(i+1) + ": Yes")
        else:
            print("Case #" + str(i+1) + ": No")
        return set1, set2
