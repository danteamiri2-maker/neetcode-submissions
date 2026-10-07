class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


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



