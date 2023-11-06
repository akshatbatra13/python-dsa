from typing import List


class Solution():
    # brute force: find two elements in the arary that add to the target -> O(n**2)
    def two_sum_bf(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1): # prevent IndexError
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return False
    
    # hashtable: find the complement of the target in the hashtable 
    def two_sum_hashtable_tp(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            hashtable[num] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable and hashtable[complement] != i:
                return [i, hashtable[complement]]
        return -1

    def two_sum_hashtable_op(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [hashtable[complement], i]
            hashtable[num] = i
        return -1

if __name__ == "__main__":
    nums = list(map(int, input().strip().split(',')))
    target = int(input())
    main = Solution()
    print(main.two_sum_hashtable_op(nums, target))
