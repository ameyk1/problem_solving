from collections import deque
class Solution:
    def letter_comb(self, x):
        letter_pad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        str_x = str(x)
        len_x=len(str_x)
        list_x =[]
        if len_x==0:
            return list_x
        x_q= deque()
        x_q.append("")
        while len(x_q)!=0:
            comb_string =x_q.pop()
            if len(comb_string) ==len_x:
                list_x.append(comb_string)
            else:
                letter_num = int(str_x[len(comb_string)])
                for letter in letter_pad[letter_num]:
                    x_q.append(comb_string+letter)
        return list_x

def main():
    sol = Solution()
    print(sol.letter_comb(""))


if __name__ == "__main__":
    main()