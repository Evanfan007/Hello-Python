a = 0
b = 1

while b < 10000 :
    a, b = b, a + b
    print(b, end=",")