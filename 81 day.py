class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        inv_count = 0
        def merge_sort(arr):
            nonlocal inv_count
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)
            sorted_arr = []
            i = j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    sorted_arr.append(left_half[i])
                    i += 1
                else:
                    sorted_arr.append(right_half[j])
                    j += 1
                   
                    inv_count += len(left_half) - i
            
            sorted_arr.extend(left_half[i:])
            sorted_arr.extend(right_half[j:])
            
            return sorted_arr
        merge_sort(arr)
        return inv_count
