class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap.get(key)

        if not values: return ""

        l = 0
        r = len(values) - 1

        best_valid = ""

        while l <= r:
            m = l + (r - l) // 2
            ts = values[m][0]

            time_diff = timestamp - ts
            
            if time_diff == 0:
                return values[m][1]

            if time_diff < 0:
                r = m - 1
            else:
                l = m + 1
                best_valid = values[m][1]

        return best_valid






        
