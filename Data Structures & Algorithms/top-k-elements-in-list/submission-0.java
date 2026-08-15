class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] topK = new int[k];
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<Integer> (k, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                return freq.get(b) - freq.get(a);
            }
        });

        for (int num: freq.keySet()) {
            pq.add(num);
        }

        int i = 0;
        while (!pq.isEmpty() && i < k) {
            topK[i++] = pq.poll();
        }
        
        return topK;
    }
}
