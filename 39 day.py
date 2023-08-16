class Solution: 
    def select(self, arr, i):
        smallest_index=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[smallest_index]):
              smallest_index=j
                
        return smallest_index
    def selectionSort(self, arr,n):
      for i in range(n):
            min=self.select(arr,i) 
            arr[i],arr[min]=arr[min],arr[i]
