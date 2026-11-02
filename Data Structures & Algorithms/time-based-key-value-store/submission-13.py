from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.seen = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.seen:
            self.seen[key] = defaultdict(str)
        self.seen[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.seen:
            return ""
        else:
            if timestamp in self.seen[key]:
                # timestamp exists
                return self.seen[key][timestamp]
            else:
                
                timestamp_prev = -1
                for t, v in self.seen[key].items():
                    if t >= timestamp:
                        break
                    timestamp_prev = max(t, timestamp_prev)
                    
                return self.seen[key][timestamp_prev]
                    

        
        

        
