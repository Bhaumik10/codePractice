## Problem
## Write a function that takes a string as input and returns the string reversed.

## Example:
## Given s = "hello", return "olleh".


## Solution
import sys

def reverseString(s):
    input_string = s        ## Give proper name to supplied argument

    rev_list = []           ## store characters in the list with reverse order
    length_input_string = len(input_string)     ## Determine the length of input

    for i in reversed(xrange(length_input_string)):     ## Logic to reverse the string
        new = input_string[i]
        rev_list.append(new)

    for j in xrange(len(rev_list)):   ## Print the desired output
        sys.stdout.write(rev_list[j]) ## I use library sys to try the print list without each letter
                                      ## In newline

## Calling the function
reverseString('Hey there !! Here we are trying to  write a code which reverse a given input string')

