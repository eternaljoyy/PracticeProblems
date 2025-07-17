# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):


def guessNumber(self, n):
    """
        :type n: int
        :rtype: int
    """ 

    ''' 
    Go through sequence of numbers using binary search. 
    '''
         
        left = 1
        right = n

        while left < right:
            midpoint = (left + right) / 2
        
            if guess(midpoint) == 0:
                return midpoint 
            elif guess(midpoint) == -1:
                left = midpoint + 1
            else:
                right = midpoint - 1