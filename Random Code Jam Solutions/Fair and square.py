def fair(x):
    num = str(x)
    if len(num)%2 == 0:
        for i in range(0, len(num)//2):
            if num[i] == num[-1-i]:
                return True
            else:
                return False
    else:
        for i in range(0, len(num)//2 + 1):
            if num[i] == num[-1-i]:
                return True
            else:
                return False

def square(x):
    from math import sqrt
    num = str(sqrt(x)).strip('.0')
    if num.find(".") != -1:
        return False
    else:
        if fair(num) == True:
            return True

def fairnsquare(filename):
    count = 0
    file = open(filename)
    testcases = int(file.readline().rstrip())
    i = 0
    print ("Test cases = " + str(testcases))
    while i < testcases :
        line = file.readline()
        var1 = int(line[:line.index(' ')])
        var2 = int(line[line.index(' ')+1:]) + 1
        for x in range(var1, var2):
            if fair(x) and square(x) == True:
                count += 1
        print ("Case #" + str(i+1) + ": " + str(count))
        i += 1
        count = 0
    file.close()
    
def test():
    count = 0
    var1 = int(input("var 1 = "))
    var2 = int(input("var 2 = "))
    for x in range(var1, var2):
            if fair(x) and square(x) == True:
                count += 1
                print (count)
