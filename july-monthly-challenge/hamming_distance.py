class Solution:
    # def hammingDistance(self, x, y):
    #     distance = 0
    #     x_bin, y_bin = self.decimal2binary(x, y)
    #     for i in range(len(x_bin)):
    #         if x_bin[i] != y_bin[i]:
    #             distance+=1
    #     return distance
    # def decimal2binary(self, x, y):
    #     return "{:032b}".format(x), "{:032b}".format(y)
    def hammingDistance(self, x, y):
        distance = 0
        while (x|y):
            distance+= (x&1) ^ (y&1)
            x >>=1
            y >>=1
        return distance


def main():
    x, y = 1, 4
    sol = Solution()
    distance = sol.hammingDistance(x, y)
    print(distance)

if __name__ == '__main__':
    main()