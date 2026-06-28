class HitCounter:

    def __init__(self):
        self.hit_map = {}        

    def hit(self, timestamp: int) -> None:
        # check if timestamp is a key in the dict
        # if so we can add 1 to the value
        if timestamp in self.hit_map.keys():
            self.hit_map[timestamp] += 1
            return
        # else add it to the hit map
        else: 
            self.hit_map[timestamp] = 1
        return
        

    def getHits(self, timestamp: int) -> int:
        hits = 0
        # look at the keys in the hit map, add up timestamps
        # that are less than or equal to the timestamp - 300 to timestamp
        min_time = max(timestamp - 299,1) # so value is never below 1
        max_time = timestamp
        # valid time steps are greater than or equal to min_time 
        # but less than or equal to the timestamp 
        for t in self.hit_map.keys():
            if (t >= min_time) and (t <= max_time):
                hits += self.hit_map[t]
        return hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
