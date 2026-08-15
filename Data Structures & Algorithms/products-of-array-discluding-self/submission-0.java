class Solution {
    public int[] productExceptSelf(int[] nums) {
       int[] res = new int[nums.length];
       Map<Integer, Integer> leftProdMap = new HashMap<>();
       Map<Integer, Integer> rightProdMap = new HashMap<>();
       int leftProd = 1;
       int rightProd = 1;
       for (int i = 0; i < nums.length; i++) {
            leftProdMap.put(i, leftProd);
            leftProd *= nums[i];
       }
       for (int j = nums.length - 1; j > - 1; j--) {
            rightProdMap.put(j, rightProd);
            rightProd *= nums[j];
       }
       for (int k = 0; k < res.length; k++) {
            res[k] = leftProdMap.get(k) * rightProdMap.get(k);
       }
       return res;
    }
}  
