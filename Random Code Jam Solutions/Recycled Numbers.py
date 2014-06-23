def recycled_numbers(filename):
    file = open(filename)
    out = open("output.txt", 'w+')
    testcases = int(file.readline())
    for test in range(0, testcases):
        A,B = file.readline().split(' ')
        A = int(A)
        B = int(B)
        count= 0
        for i in range(A, B+1):
            var = str(i)
            for j in range(1, len(var)):
                var2 = int(var[j:] + var[:j])
                if var2 == i:
                    break
                if A <= i < var2 <= B:
                    count += 1
        out.write("Case #" + str(test+1) + ": " + str(count) + '\n')
