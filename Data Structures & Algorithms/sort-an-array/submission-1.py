class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Time Complexity -> O(nlog(n))
        # Space Complexity -> O(n)

        def merge_elements(array, left, mid, right):
            left_half = array[left:mid+1]
            right_half = array[mid+1:right+1]

            i = left
            j = 0 
            k = 0

            while j < len(left_half) and k < len(right_half):
                if left_half[j] <= right_half[k]:
                    array[i] = left_half[j]
                    j += 1
                else:
                    array[i] = right_half[k]
                    k += 1
                i += 1

            while j < len(left_half):
                array[i] = left_half[j]
                j += 1
                i += 1

            while k < len(right_half):
                array[i] = right_half[k]
                k += 1
                i += 1


        def merge_sort(array, left, right):
            if left == right:
                return array

            mid = (left + right) // 2

            merge_sort(array, left, mid)
            merge_sort(array, mid + 1, right)

            merge_elements(array, left, mid, right)

            return array

        return merge_sort(nums, 0, len(nums) - 1)