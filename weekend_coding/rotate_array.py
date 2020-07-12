class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_num = len(nums)
        k%=len_num
        if k==0:
            return nums
        self.reverse_array(nums, 0, len_num-1)
        self.reverse_array(nums, 0,k-1)
        self.reverse_array(nums, k,len_num-1)
        print(nums)
    def reverse_array(self, list_num, start, end):
        mid_index = int((start+end)/2)
        i=0
        while start+i <= mid_index:
            temp=list_num[start+i]
            list_num[start+i]=list_num[end-i]
            list_num[end-i]=temp
            i+=1
def main():
    sol=Solution()
    nums = [1,2,3,4,5,6,7]
    k=3
    sol.rotate(nums, k)
if __name__ == "__main__":
    main()

