x = int(input("Enter the number upto which we have to find the fibonacci series"))

m = 0
n = 1

for i in range(0, x):
    p = m + n
    print(m)
    m = n
    n = p
