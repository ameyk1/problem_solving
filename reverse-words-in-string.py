class Solution:
    def reverseWords(in_string):
        in_array = str(in_string).split()
        return ' '.join(in_array[::-1])
def main():
    in_string = "  hello world!  "
    sol = Solution
    array = sol.reverseWords(in_string=in_string)
    print(array)
if __name__ == '__main__':
    main()