class Solution:
    def lenthOfLongestSubstring(self, s: str) -> int:
        count, longestCount = 0, 0
        # enumerate iteration give index and value at the time
        for key, value in enumerate(s):
            # Check index not equals last index to intercept index out of bound
            # Check current value with next value, if equal reset count to 0
            if key != len(s) - 1 and value == s[key + 1]:
                # Set count as longestCount value if count greater than longestCount
                longestCount = count if count > longestCount else longestCount
                # Reset count if current value equal with next value
                count = 0
            count += 1
        return longestCount


if __name__ == "__main__":
    s = "abrkaabcdefghijjxxx"
    length = Solution().lenthOfLongestSubstring(s)
    assert length == 10, "%s is not 10" % length
    print("Passed Test")
