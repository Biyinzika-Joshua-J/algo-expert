def merge( intervals):
        intervals.sort()
        result = [intervals[0]]
        if len(intervals) == 1:
            return intervals
        for idx, interval in enumerate(intervals):
            if idx == 0:
                continue
            if interval[0] <= result[-1][1]:
                if interval[1] > result[-1][1]:
                    result[-1][1] = interval[1]
            else:
                result.append(interval)
        return result
