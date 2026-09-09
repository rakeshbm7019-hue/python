from functools import lru_cache

def longest_increasing_subsequence(nums):
    @lru_cache(None)
    def lis_ending_at(i):
        best = 1
        for j in range(i):
            if nums[j] < nums[i]:
                best = max(best, lis_ending_at(j) + 1)
        return best

    return max(lis_ending_at(i) for i in range(len(nums)))

arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", longest_increasing_subsequence(arr))
