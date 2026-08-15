class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqbucket = [[] for i in range(len(nums))]
        freqmap = dict.fromkeys(nums, 0) 
        # prepare frequency map
        for num in nums:
            freqmap[num] += 1

        # prepare array for bucket sort (sorting based on freq)
        for num, freq in freqmap.items():
            freqbucket[freq - 1].append(num)

        # traverse in reverse order in the frequency array
        result = []
        count = 0
        for item in freqbucket[::-1]:
            for val in item:
                if count == k:
                    break
                result.append(val)
                count += 1
        return result

            


    

