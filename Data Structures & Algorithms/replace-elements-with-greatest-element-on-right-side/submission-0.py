class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        
        for i in range(0, len(arr) - 1):
            greatest_num = arr[i+1]

            for j in range(i+1, len(arr)):
                if arr[j] > greatest_num:
                    greatest_num = arr[j]
            
            if greatest_num >= arr[i+1]:
                arr[i] = greatest_num
        
        arr[-1] = -1

        return arr
            


        