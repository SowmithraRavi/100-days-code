class Solution:
    def merge(self,arr, l, m, r): 
        pass
    def mergeSort(self,arr, l, r):
        if len(arr) > 1:
            mid=len(arr)//2 
            left_array=arr[:mid]
            right_array=arr[mid:]
            
            self.mergeSort(left_array,l,mid)
            self.mergeSort(right_array,mid,r) 
            i=0
            j=0
            k=0 
            while(i<len(left_array) and j<len(right_array)):
                if(left_array[i]<right_array[j]):
                    arr[k]=left_array[i]
                    i+=1
                else:
                    arr[k]=right_array[j]
                    j+=1 
                k+=1 
            while(i<len(left_array)):
                arr[k]=left_array[i]
                i+=1 
                k+=1
            while(j<len(right_array)):
                arr[k]=right_array[j]
                j+=1 
                k+=1
