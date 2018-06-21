# 344. Reverse String

# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh". 

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Accepted
        # s=s[::-1]
        # return s 
        
        # Got time limit exceeded for this code
        # str = ""
        # for i in s:
        #     str = i + str
        # return str
        
        # Accepted
        string = "".join(reversed(s))
        return string
        
        