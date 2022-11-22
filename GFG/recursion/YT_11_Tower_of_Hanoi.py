# Tower of Hanoi
# GFG : https://practice.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1


# class Solution:
#     count = 0
#     def toh(self, s, d, h, n):
#         # My base condition
#         self.count += 1
#         if n == 1:
#             print(f"move disk {n} from rod {s} to rod {d}")
#             return self.count
#
#         self.toh(s, h, d, n - 1)
#         print(f"move disk {n} from rod {s} to rod {d}")
#         self.toh(h, d, s, n - 1)
#
#         return self.count
class Solution:
    count = 0
    def toh(self, s, d, h, n):
        # My base condition
        self.count += 1
        if n == 1:
            print("move disk {0} from rod {1} to rod {2}".format(n, s, d))
            return self.count

        self.toh(s, h, d, n - 1)
        print("move disk {0} from rod {1} to rod {2}".format(n, s, d))
        self.toh(h, d, s, n - 1)

        return self.count

def main():
    T = int(input())

    while T > 0:
        N = int(input())
        ob = Solution()
        print(ob.toh(1, 3, 2, N))
        T -= 1


if __name__ == '__main__':
    main()
