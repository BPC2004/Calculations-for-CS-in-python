
# Python3 program to calculate
# Fibonacci no. modulo m using
# Pisano Period
 
# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m 
def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
         
        if (previous == 0 and current == 1):
            return i + 1

def fibonacciModulo(n, m):

    pisano_period = pisanoPeriod(m)

    n = n % pisano_period
     
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, previous + current
         
    return (current % m)

if __name__ == '__main__': 
    n = 16
    m = 1
    print(fibonacciModulo(n, m))
