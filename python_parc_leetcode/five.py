class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s =''
        for i in digits:
            s +=str(i)
        digits.clear()
        ans = str(int(s)+1)
        for i in range(len(ans)):
            digits.append(int(ans[i]))
        return digits
