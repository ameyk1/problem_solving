# July Monthly Challenge
# Some hints from here: https://youtu.be/kSDI_iOiGQY

class Solution:
    def nthUglyNumber(self, n):
        ugly_num_list = [0]*n
        ugly_num_list[0]=1
        i = 1
        idx2, idx3, idx5 = 0, 0, 0
        while i < n:
            nxt2 = ugly_num_list[idx2]*2
            nxt3 = ugly_num_list[idx3]*3
            nxt5 = ugly_num_list[idx5]*5
            next_elem = min(nxt2, nxt3, nxt5)
            if next_elem == nxt2:
                idx2 +=1
            if next_elem == nxt3:
                idx3 +=1
            if next_elem == nxt5:
                idx5 +=1
            ugly_num_list[i] = next_elem
            i += 1
        print(ugly_num_list)
        return ugly_num_list[-1]



def main():
    n = 99
    sol = Solution()
    n_ugly = sol.nthUglyNumber(n)
    print(n_ugly)
if __name__ == '__main__':
    main()