from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counter = Counter(nums) 
        #sorted_counter = sorted(counter.items(), key=lambda item: item[1])
     
        for _ in range(k):
            most_frequent_num = max(counter, key=counter.get)
            ans.append(most_frequent_num)
            counter.pop(most_frequent_num)
            
        return ans

        