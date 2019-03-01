'''

Create a function named divisors/Divisors that takes an integer n > 1
and returns an array with all of the integer's divisors(except for 1
and the number itself), from smallest to largest. If the number is
prime return the string '(integer) is prime'

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

Solution by
Ednalyn C. De Dios

'''


def divisors(n):
    a = [] # the array
    for x in range(2, n-1): # generates numbers from 2 to n-1
        if n % x == 0: # if n divided by x has no remainder
            a.append(x) # n is divisible by x so add it to array

    if len(a) == 0: # if the array is empty
        return str(n) + ' is prime' # n is a prime number
    else:    
        return a # divisors of n