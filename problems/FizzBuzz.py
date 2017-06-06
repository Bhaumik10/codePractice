## Problem Statement
## Write a program that outputs the string representation of numbers from 1 to n.
## But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

## Solution::

def fizzBuzz(self,n):
    for number in xrange(1,n+1): ## We will start the Index with 1.
        if number % 15 == 0:
            n_ = "FizzBuzz"
            self.append(n)
        elif number % 3 == 0:
            n_ = "Fizz"
            self.append(n)
        elif number % 5 == 0:
            n_ = "Buzz"
            self.append(n)
        else:
            self.append(str(number))
    return self

answer = fizzBuzz([],15)

print answer



