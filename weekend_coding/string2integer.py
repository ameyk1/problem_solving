import re
class Solution:
   def myAtoi(self,x):
     x = x.lstrip()
     if not x:
        return 0
     else:
        if x[0]=='-':
          sign =-1
          x = x[1:]
        elif x[0]=='+':
          sign =1
          x = x[1:]
        else:
          sign=1
        if not x:
          return 0
        if not x[0].isnumeric():
          return 0
        else:
            x=re.split('[a-z]|[.]|[,]|[;] |[" "]|[-]|[+]',x)
            if (int(x[0])*sign > int(2147483647)):
              return int(2147483647)
            elif (int(x[0])*sign < int(-2147483648)):
              return int(-2147483648)
            else:
              return int(x[0])*sign
def main():
   num="    +0 123"
   sol=Solution()
   x =sol.myAtoi(num)
   print(x)
if __name__ == "__main__":
   main()

