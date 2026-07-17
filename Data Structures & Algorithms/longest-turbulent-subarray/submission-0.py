class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        from collections import deque

        window = deque()

        l = 0
        r = len(arr)
        max_window_len = 0

        prev_sign = None

        while l<r:
            if l==0:
                window.append(arr[l])
                max_window_len = max(max_window_len,len(window))
                l+=1
            elif prev_sign == -1 and window[-1] < arr[l]:
                prev_sign = 1
                window.append(arr[l])
                l+=1
                max_window_len = max(max_window_len,len(window))
            elif prev_sign == 1 and window[-1] > arr[l]:
                prev_sign = -1
                window.append(arr[l])
                l+=1
                max_window_len = max(max_window_len,len(window))
            elif not prev_sign and window[-1] < arr[l]:
                prev_sign = 1
                window.append(arr[l])
                l+=1
                max_window_len = max(max_window_len,len(window))
            elif not prev_sign and window[-1] > arr[l]:
                prev_sign = -1
                window.append(arr[l])
                l+=1
                max_window_len = max(max_window_len,len(window))
            else:
                window.clear()
                if arr[l - 1] == arr[l]:
                    window.append(arr[l])
                    l += 1
                else:
                    window.append(arr[l - 1])
                prev_sign = None
        return max_window_len