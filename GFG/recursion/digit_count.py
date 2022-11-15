#User function Template for python3

class Solution:
    def countDigits(self, n):
        '''
        :param n: given number
        :return: count of digits of n.
        '''
        # code here

        # base case
        if n < 10:
            return 1

        return 1 + self.countDigits(n // 10)