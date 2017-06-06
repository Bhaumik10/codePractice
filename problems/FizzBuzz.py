Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Solution::

def fizzBuzz(self,n):
    for i in xrange(1,n+1):
        if i % 15 == 0:
            n = "FizzBuzz"
            self.append(n)
        elif i % 3 == 0:
            n = "Fizz"
            self.append(n)
        elif i % 5 == 0:
            n = "Buzz"
            self.append(n)
        else:
            self.append(str(i))
    return self

answer = fizzBuzz([],15)

print answer



