class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def quickSort(arr):
        #     if len(arr)<=1:
        #         return arr
        #     pivot = arr[0]
        #     left = [i for i in arr[1:] if i<=pivot]
        #     right = [i for i in arr[1:] if i>pivot]
        #     return quickSort(left) + [pivot] + quickSort(right)
        # return quickSort(nums)

        def mergeSort(arr):
            width = 1
            n = len(arr)
            while width < n:
                for i in range(0, n, width * 2):
                    left = arr[i:i+width]
                    right = arr[i+width:i+width*2]
                    merged = []
                    l = r = 0
                    while l < len(left) and r< len(right):
                        if left[l] <= right[r]:
                            merged.append(left[l])
                            l+=1
                        else:
                            merged.append(right[r])
                            r+=1
                    merged.extend(left[l:])
                    merged.extend(right[r:])
                    arr[i:i + len(merged)] = merged
                width *= 2
            return arr
        return mergeSort(nums)
