class Solution:
    def maxArea(self, x):
        max_area = 0
        container_x = len(x)-1
        container_y =0
        while container_x != container_y:
            if x[container_x] > x[container_y]:
                container_area = x[container_y]* (container_x - container_y)
                container_y+=1
            else:
                container_area = x[container_x] * (container_x - container_y)
                container_x-=1
            max_area = max(max_area,container_area)
            #print('Container Area: {} \t Max Area: {}'.format(container_area,max_area))
        return max_area

def main():
    sol = Solution()
    container_cord=[1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(container_cord))


if __name__ == "__main__":
    main()