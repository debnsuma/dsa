
class Solution:
    count = 0
    def substring(self, input_string, output_string):

        # My base condition
        if len(input_string) == 0:
            print(output_string)
            self.count += 1
            return self.count

        # When we are considering UPPER case of the first char
        self.substring(input_string[1:], output_string + input_string[0].upper())


        # When we are considering LOWER case of the first char
        self.substring(input_string[1:], output_string + input_string[0].lower())

        return self.count

def main():
    T = int(input())

    while T > 0:
        input_string = input()
        output_string = ""
        ob = Solution()
        print(ob.substring(input_string, output_string))
        T -= 1


if __name__ == '__main__':
    main()


