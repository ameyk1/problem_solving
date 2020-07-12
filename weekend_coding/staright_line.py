class Solution:
    def checkStraightLine(self, x):
        len_x = len(x)-1
        slope_list=[]
        for i in range (len_x):
            slope_list.append(self.check_line_slope(x[i],x[i+1]))

        if self.chkList(slope_list)==True:
            return True
        else:
            return False
    def check_line_slope(self,pt1,pt2):
        try:
            return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        except ZeroDivisionError:
            return 0

    def chkList(self,lst):
        return len(set(lst)) == 1

def main():
    sol = Solution()
    line_cord=[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    #line_cord =[[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
    print(sol.checkStraightLine(line_cord))


if __name__ == "__main__":
    main()