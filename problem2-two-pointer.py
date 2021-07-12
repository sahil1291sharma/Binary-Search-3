class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr)-1
        
        while (end - start + 1) > k:
            distLow = abs(x-arr[start])
            distHigh = abs(x-arr[end])
            if distLow >= distHigh:
                start +=1
            else:
                end -=1
        result =[]        
        for i in range(start, end):
            result.append(arr[i])
        return result