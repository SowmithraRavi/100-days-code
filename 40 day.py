class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if(arr[i] > arr[j]):
                  arr[i],arr[j] = arr[j],arr[i]
                
        return arr
