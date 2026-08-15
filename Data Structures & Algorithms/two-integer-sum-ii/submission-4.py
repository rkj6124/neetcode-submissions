class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset = defaultdict(list)
        for i in range(len(numbers)):
            n = numbers[i]
            numset[n].append(i + 1)
        

        for key in numset.keys():
            if target - key in numset:
                if key == target - key:
                    return [numset[key][0], numset[key][1]]
                return sorted([numset[key][0], numset[target - key][0]])