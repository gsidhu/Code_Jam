def factorial(x):
    for i in range(1, x):
        x *= i
    return x

def multiply(a,b):
    c = 0
    for i in range(0, len(a)):
        c += int(a[i])*int(b[i])
    return c

def shuffle(a):
	b = a
	count = 0
	for i in range(0, len(a)):
		for j in range(0, len(a)):
			if j != i:
				if j != 0:
					var = a[j]
					a[j] = a[-j]
					a[-j] = var
					return a
				else:
					var = a[j]
					a[j] = a[-1]
					a[-1] = var
					return a

def msp(filename):
    file = open(filename)
    testcases = int(file.readline().rstrip())
    count = 0
    
    while count < testcases :
        size = int(file.readline())
        var1 = file.readline().split(" ")
        var2 = file.readline().split(" ")
        product = []
        index = 0

        while index < factorial(size):
            product.append(multiply(var1,var2))
            shuffle(var1)
            index += 1
        product.sort()
        
        print("Case #" + str(count+1) + ": " + str(product[0]))
        count += 1
    
