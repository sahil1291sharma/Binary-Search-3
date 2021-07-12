class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr)-1
        
        while (end - start + 1)  > k:
            distLow = abs(x-arr[start])
            distHigh = abs(x-arr[end])
            if distLow > distHigh:
                start +=1
            else:
                end -=1
        
        return arr[start:start+k]

#Time complexity is O(logN-K) where n is the number of elements in the input and K is the number of elements to be returned
#Space complexity is O(1) 