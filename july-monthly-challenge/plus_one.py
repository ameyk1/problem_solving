class Solution:
    def plusOne(self, digits):
        len_digits = len(digits)-1
        new_digit = 0
        for digit in digits:
            new_digit+= digit*10**(len_digits)
            len_digits-=1
        new_digit_str = str(new_digit + 1)
        if digits[0] == 0 and (len(digits)-1)>0:
            new_digit_str = str("0")+new_digit_str

        new_digits =list(map(int, new_digit_str))
        return new_digits
        # new_digit = 1
        # for idx, digit in enumerate(digits[::-1]):
        #     new_digit += (digit*10**idx)
        # return list(str(new_digit))

def main():
    digits = [0, 1, 2]
    sol = Solution()
    plus_one_digits = sol.plusOne(digits)
    print(plus_one_digits)

if __name__ == '__main__':
    main()