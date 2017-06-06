## Problem Statement
## Given an array of integers, every element appears twice except for one. Find that single one.

## Note:
## Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Solution


def singleNumber(nums):

    end_pt = len(nums)              ## getting the length of input array
    for i in range(0, end_pt, 2):   ## Looping through the array
        if i == end_pt - 1:
            print nums[i]           ## If we reach at end of array then last element
                                    ## is single
        elif nums[i] != nums[i+1]:  ## Normally mapping the adjucent elements
            print nums[i]
            break                   ## Once you detect single number break it


## Calling the function
singleNumber([2,2,1,3,3])
