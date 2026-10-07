class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binarySearchSolution(numbers, target):

            for i in range(len(numbers) - 1):

                l, r = i + 1, len(numbers) - 1
                complement = target - numbers[i]
                while l <= r:
                    m = l + (r - l) // 2

                    if numbers[m] == complement:
                        return [i + 1, m + 1]
                    
                    if numbers[m] < complement:
                        l = m + 1
                    
                    if numbers[m] >= complement:
                        r = m - 1

            return []
        
        def twoPointerSolution(numbers, target):

            l, r = 0, len(numbers)-1

            while l < r:
                curr_sum = numbers[l] + numbers[r]

                if curr_sum > target:
                    r -= 1
                if curr_sum < target:
                    l += 1
                if curr_sum == target:
                    return [l+1, r+1]
            
            return []

        return twoPointerSolution(numbers, target)



