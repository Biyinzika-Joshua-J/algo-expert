def LongestPeak(array):
    pass

def longestMountain( arr):
        peaks = []
        
        if len(arr) == 1:
            if arr[0] == 0:
                return 0
            return 1
        for idx in range(len(arr)):
            if idx == 0:
                continue
            if idx == len(arr)-1:
                continue
            if arr[idx-1] < arr[idx] and arr[idx+1] < arr[idx]:
                peaks.append(idx)
        length = 0
        for peak in peaks:
            peakLength = getPeakLength(peak, arr, peaks)
            length = max(peakLength, length)
        return length

def getPeakLength(peak, arr, peaks):
    highest = peak
    # get length to the left
    leftIndex = peak-1
    length = 1

    while leftIndex >= 0 and arr[leftIndex] < arr[leftIndex+1]:
        length += 1
        leftIndex -= 1

    rightIndex = peak+1
    while rightIndex < len(arr) and arr[rightIndex] < arr[rightIndex-1]:
        length += 1
        rightIndex += 1
    
    return length
    



peaks = [1,2,3,3,4,0,10,6,6,5,-1,-3,2,3]
print(longestMountain(peaks))