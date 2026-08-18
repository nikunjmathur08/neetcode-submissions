class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set()
        streak = 1
        if not nums:
            return 0
        
        for i in nums:
            num.add(i)
        
        for i in nums:
            if i-1 not in num:
                currentStreak = 1
                while (i+1 in num):
                    currentStreak += 1
                    streak = max(streak, currentStreak)
                    i += 1
        return streak
