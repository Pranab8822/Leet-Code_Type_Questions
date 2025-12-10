class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies manually
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Step 2: Convert to list of (num, freq)
        freq_list = []
        for key in freq_map:
            freq_list.append((key, freq_map[key]))

        # Step 3: Sort by frequency (descending)
        freq_list.sort(key=lambda x: x[1], reverse=True)

        # Step 4: Take top k elements
        result = []
        for i in range(k):
            result.append(freq_list[i][0])

        return result
        