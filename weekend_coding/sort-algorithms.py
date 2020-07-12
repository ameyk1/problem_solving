class count_sort():
    # Understood CountSort from: https://www.geeksforgeeks.org/counting-sort/
    # Time Complexity: O(n+k), where n is number of elements and k is range of inputs
    # Space Complexity: O(n+k)
    def count_sort_unsigned(self,unsorted_arr):
        output = [0 for i in range (len(unsorted_arr))]
        count_len = max(unsorted_arr) # Length of the count index array
        print("Unsorted Input Array", unsorted_arr)
        count_arr = [0 for i in range (count_len+1)]
        # Step1:
        for i in range (0,len(unsorted_arr)):
            count_arr[unsorted_arr[i]]+=1
        # Add two side by side
        for i in range (1, len(count_arr)):
            count_arr[i]+=count_arr[i-1]
        for i in range (0, len(unsorted_arr)):
            output[count_arr[unsorted_arr[i]]-1] = unsorted_arr[i]
            count_arr[unsorted_arr[i]] -=1
        print(output)

    def count_sort_sign(self, unsorted_arr):
        max_len = max(unsorted_arr)
        min_len = min(unsorted_arr)
        range_array = max_len - min_len +1
        print("Unsorted Input Array", unsorted_arr)
        output = [0 for i in range(len(unsorted_arr))]
        count_arr = [0 for i in range(range_array)]
        # Step1:
        for i in range(0, len(unsorted_arr)):
            count_arr[unsorted_arr[i]-min_len] += 1
        for i in range (1, len(count_arr)):
            count_arr[i]+=count_arr[i-1]
        for i in range (0, len(unsorted_arr)):
            output[count_arr[unsorted_arr[i]-min_len]-1] = unsorted_arr[i]
            count_arr[unsorted_arr[i]-min_len] -=1
        return output

class quick_sort():

    def partition(self, arr, low_index, high_index):
        pivot = arr[high_index]
        smaller_index = low_index - 1
        for j in range(low_index, high_index):
            if arr[j] < pivot:
                smaller_index+=1
                arr[smaller_index], arr[j] = arr[j], arr[smaller_index]
        arr[smaller_index+1], arr[high_index] = arr[high_index], arr[smaller_index+1]
        return smaller_index+1

    def quick_sort_funct(self, arr, low_index, high_index):
        if low_index < high_index:
            pi = self.partition(arr, low_index, high_index)
            self.quick_sort_funct(arr, low_index, pi-1)
            self.quick_sort_funct(arr, pi+1, high_index)
        return arr

def main():
    unsorted_arr = [1,-4,1,2,7,5,2, 10, 11 ,6,6]
    # Count Sort
    _count_sort = count_sort()
    sorted_array = _count_sort.count_sort_sign(unsorted_arr)
    print("Count Sort Output", sorted_array)
    # Quick Sort
    _quick_sort = quick_sort()
    sorted_array = _quick_sort.quick_sort_funct(unsorted_arr,0, len(unsorted_arr)-1)
    print("Quick Sort Output", sorted_array)

if __name__ == "__main__":
    main()



