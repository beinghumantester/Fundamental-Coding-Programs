x = int(input("Enter the number upto which we have to find the fibonacci series"))

# Taking 3 variables - 2 for previous and current, while 3rd for storing their sum

m = 0
n = 1

for i in range(0, x):
    p = m + n
    print(m)  # on every loop printing previous variable's value
    m = n  # updating previous variable with current variable
    n = p  #updating current variable with sum of last two variables i.e last current and last previous
