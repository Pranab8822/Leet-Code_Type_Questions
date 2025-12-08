class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
    
    # Step 2: Find first non-repeating
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
    
    # Step 3: If none found
        return -1
        