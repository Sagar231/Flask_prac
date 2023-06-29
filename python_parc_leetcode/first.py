class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        temp = []
        if len(intervals)==1:
            return intervals
        intervals.sort()
        def checkmerge(l1,l2):
            if l1[1]>=l2[0]:
                return [l1[0],l2[1]]
            return -1

        for i in range(0,len(intervals)-1):
            m = checkmerge(intervals[i],intervals[i+1])
            if m == -1:
                continue
            intervals[i+1] = m
            temp.append(i)
        for i in temp:
            intervals.pop(i)
        return intervals
