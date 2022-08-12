class TimeMap(object):

    def __init__(self):
        self.keyStore = {} # key: list of [val, timestamp]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # if the key is already in the store, if not, we are gonna add one
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # binary search
        res = ""
        values = self.keyStore.get(key, []) # in case we get nothing and meet the error; Get all the values with the same key, then we apply binary search(on timestamp) to find the exactly match
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # (val, timestamp), the index of timestamp is 1
                res = values[m][0]
                l = m + 1
            else: # 违规了
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)