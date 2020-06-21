#
# @lc app=leetcode.cn id=1 lang=java
#
# [1] two-sum
#
class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> map = new HashMap();
        
        for (int i = 0; i < nums.length; ++i) {
            if (map.containsKey(target- nums[i])) 
                return new int[]{map.get(target- nums[i]), i};
            map.put(nums[i], i);
        }
        return new int[2];
    }
}
# @lc code=end