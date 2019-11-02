class Solution:
    def reverse(self, x):
        sign = self.sign_num(x)
        str_x = str(abs(x))
        conv_str = 0
        j= len(str_x)
        for i in range (len(str_x),0,-1):
            j-=1
            conv_str+=int(str_x[i-1])*10**j
        
        conv_str*=sign
        if abs(conv_str) > 0x7FFFFFFF:
            return 0
        else:
            return conv_str
    def sign_num(self,x):
        if (x<0):
            sign=-1
        elif (x>0):
            sign=1
        else:
            sign=1
        return sign
def main():
    sol = Solution()
    print(sol.reverse(-123))

if __name__ =="__main__":
    main()
