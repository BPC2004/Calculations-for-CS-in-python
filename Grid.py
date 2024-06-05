
# Python3 implementation of above approach 
 
# function that will calculate the factorial 
def factorial(N) : 
     
    result = 1; 
     
    while (N > 0) :
         
        result = result * N; 
        N -= 1; 
     
    return result; 
 
def countWays(N) : 
 
    total = factorial(N + N); 
    total1 = factorial(N); 
     
    return (total // total1) // total1; 
 
# Driver code 
if __name__ == "__main__" : 
 
    N = 4; 
     
    print("Ways =", countWays(N)); 
 
# This code is contributed by Ryuga
