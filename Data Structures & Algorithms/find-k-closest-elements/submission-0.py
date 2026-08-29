class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Time Complexity -> O(log(n))
        # Space Complexity -> O(1)
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]