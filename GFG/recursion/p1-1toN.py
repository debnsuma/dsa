class Solution:
    # Complete this function
    def printNos(self, N):
        # Base case
        if N == 1:
            print(1, end=" ")
            return

        # Induction
        self.printNos(N - 1)
        print(N, end=" ")
