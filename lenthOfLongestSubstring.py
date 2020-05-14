# Solution made by @ebysofyan
class Solution:
    def lenthOfLongestSubstring(self, s: str):
        count, longestCount = 0, 0
        for k, v in enumerate(s):
            # Check index not equals last index to intercept index out of bound
            # Check current value with next value, if equal reset count to 0
            if k != len(s) - 1 and v == s[k + 1]:
                # Set count as longestCount value if count greater than longestCount
                longestCount = count if count > longestCount else longestCount
                count = 0
            count += 1
        return longestCount


if __name__ == "__main__":
    s = "abrkaabcdefghijjxxx"
    length = Solution().lenthOfLongestSubstring(s)
    assert length == 10, "%s is not 10" % length
    print("Passed Test")
