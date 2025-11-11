class Sort:
    def __init__(self):
        self.num1 = [4, 5, 0, 0]
        self.num2 = [6, 7]
        self.m=2
        self.n=len(self.num2)

    def merge(self):
        i = self.m - 1
        j = self.n - 1
        k = self.m + self.n - 1

        while i >= 0 and j >= 0:
            if self.num1[i] > self.num2[j]:
                self.num1[k] = self.num1[i]
                i -= 1
            else:
                self.num1[k] = self.num2[j]
                j -= 1
            k -= 1

        while j >= 0:
            self.num1[k] = self.num2[j]
            j -= 1
            k -= 1

s = Sort()
s.merge()
print(s.num1)           