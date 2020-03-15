class Solution:
    def isHappy(self, n):
        if len(str(n)) == 0:
            return False
        else:
            dict = {}
            dict[n] = True
            while n != 1:
                n = self.sum_square(str(n))
                print(n)
                if n in dict:
                    return False
                else:
                    dict[n] = True
            return True
    def sum_square(self, n_str):
        sum_str = 0
        for i in range(len(n_str)):
            sum_str += int(n_str[i])**2
        return sum_str

def main():
    n= 19
    sol = Solution()
    print(sol.isHappy(n))

if __name__ == '__main__':
    main()