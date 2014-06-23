def credit(filename):
    file = open(filename)
    testcases = int(file.readline().rstrip())
    count = 0
    print ("Test cases = " + str(testcases))
    while count < testcases :
        credit = int(file.readline())
        items = int(file.readline())
        line = file.readline()
        nums = line.split(" ") 

        for i in range(0,items):
            if int(nums[i]) < credit:
                var1 = int(nums[i])
                for j in range(0, items):
                    if j != i:
                        var2 = int(nums[j])
                        if var1 + var2 == credit:
                            ans1 = i+1
                            ans2 = j+1
                            break
        count += 1
        print("Case #" + str(count) + ": " + str(ans2) + " " + str(ans1))
