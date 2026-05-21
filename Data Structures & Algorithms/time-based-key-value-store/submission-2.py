class TimeMap:

    def __init__(self):
        # key -> [array of (timestamp, value) tuples]
        self.treeDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key -> [array of (timestamp, value) tuples]
        if key in self.treeDict:
            self.treeDict[key].append((timestamp, value))
        else:
            self.treeDict[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # get the array corresponding to the key and search for timestamp
        if not self.treeDict:
            return ""
        
        if key not in self.treeDict:
            return ""
        
        timestamp_value_pairs = self.treeDict[key]
        
        # does this timestamp occur BEFORE all values?
        if timestamp < timestamp_value_pairs[0][0]:
            return ""
        
        left = 0
        right = len(timestamp_value_pairs) - 1
        best = ""

        while left <= right:
            # look for the latest possible value that occured at or before this timestamp
            mid = (left + right) // 2

            mid_timestamp = timestamp_value_pairs[mid][0]

            # this is where it changes from latest to occuring after this timestamp                
            
            # normal binary search
            if mid_timestamp <= timestamp:
                # check right side
                best = timestamp_value_pairs[mid][1]
                left = mid + 1
            elif mid_timestamp > timestamp:
                right = mid - 1
        
        return best





