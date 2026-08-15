class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // bucket sort with key as the count and value as the list of integers
        Set<Integer> topKSet = new HashSet<>();
        Set<Integer>[] buckets = new HashSet[nums.length + 1];

        Map<Integer, Integer> freq = new HashMap<>();
        for (Integer num: nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        for (int num: freq.keySet()) {
            int frequency = freq.get(num);
            Set<Integer> numsInFrequency = buckets[frequency];
            if (numsInFrequency == null) {
                numsInFrequency = new HashSet<>();
            }
            numsInFrequency.add(num);
            buckets[frequency] = numsInFrequency;
        }
        
        int count = k;
        for (int i = buckets.length - 1; i > 0 && count > 0; i--) {
            Set<Integer> numsAtIndexi = buckets[i];
            if (numsAtIndexi != null) {
                topKSet.addAll(numsAtIndexi);
                count -= numsAtIndexi.size();
            }
        }

        
        return topKSet.stream().mapToInt(Number::intValue).toArray();
    }
}