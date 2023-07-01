def reversePairs(self, nums: List[int]) -> int:
        def merge(arr,low,mid,high):
            temp = []  
            left = low  
            right = mid + 1  

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]
        
        def cntpair(arr,low,mid,high):
            cnt = 0
            right = mid+1
            for i in range(low,mid+1):
                while right <= high and  arr[i]>2*arr[right]:
                    right +=1
                cnt+=(right-(mid+1))
            return cnt

        def mergesort(arr,low,high):
            cnt = 0
            if low>=high:
                return cnt
            mid = floor((low+high)/2)
            cnt+=mergesort(arr,low,mid)
            cnt+=mergesort(arr,mid+1,high)
            cnt+=cntpair(arr,low,mid,high)
            merge(arr,low,mid,high)
            return cnt
