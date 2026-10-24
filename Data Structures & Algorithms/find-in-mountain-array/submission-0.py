class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Find the peak element
        left = 1
        right = length - 2

        while left <= right:
            mid = left + (right - left) // 2
            arrLeft = mountainArr.get(mid - 1)
            arrMid = mountainArr.get(mid)
            arrRight = mountainArr.get(mid + 1)

            if arrLeft < arrMid < arrRight:
                left = mid + 1
            elif arrLeft > arrMid > arrRight:
                right = mid - 1
            else:
                break
        peak = mid

        # Search in the left portion
        left = 0
        right = peak - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = mountainArr.get(mid)
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid

        # Search in the right portion
        left = peak
        right = length - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = mountainArr.get(mid)
            if val > target:
                left = mid + 1
            elif val < target:
                right = mid - 1
            else:
                return mid
        
        return - 1





















