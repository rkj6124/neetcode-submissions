class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> freq = new HashMap<>();
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
            index.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int remainder = target - nums[i];
            freq.put(nums[i], freq.get(nums[i]) - 1);
            if (freq.get(nums[i]) == 0) {
                // freq.remove(nums[i]);
                index.remove(nums[i]);
                // System.out.printf("Removed %d\n", nums[i]);
            }
            if (index.getOrDefault(remainder, -1) != -1) {
                return new int[] {i, index.get(remainder)};
            }
        }
        return new int[] {-1, -1};
    }
}
