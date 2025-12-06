class Solution(object):
    def secondHighest(self, s):
        element = set()
        for i in s:
            if i.isdigit():
                element.add(int(i))
        
        if len(element) < 2:
            return -1
        
        new = sorted(element, reverse=True)
        return new[1]