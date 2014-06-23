def reverse(filename):
    file = open(filename)
    testcases = int(file.readline().rstrip())
    count = 0

    while count < testcases :
        line = file.readline()
        words = line.split(" ")
        print("Case #" + str(count+1) + ":", end=" ")
        for i in range(0, len(words)):
            print(words[-1-i].strip(), end=" ")

        print("")
        count += 1
