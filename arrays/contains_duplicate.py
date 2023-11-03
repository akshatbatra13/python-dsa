from typing import List


class Solution:
    # brute force: compare each element with every other element in the list -> O(n**2)
    def contains_duplicate_bf(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # sorting: sort the elements and check if adjacent element is the same -> O(n**2)
    def contains_duplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return True
        return False

    # hashset: store values already seen in a set -> O(n)
    def contains_duplicate_hashset(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    main = Solution()
    print(main.contains_duplicate_hash(nums))
