#
# @lc app=leetcode.cn id=153 lang=java
#
# [153] find-minimum-in-rotated-sorted-array
#
class Solution {
    public int findMin(int[] nums) {
        int l =0;
        int r = nums.length -1;
         //if there is only 1 element, OR no rotation
        if(r==0 || nums[r]>nums[l]) return nums[0]; 
        
        while(r>=l){
            int mid = (l+r)/2; //mid is the left-between element due to rounding
            // at point of change, mid+1 element is the smallest
            if(nums[mid]>nums[mid+1]) return nums[mid+1];
            // at point of change, mid element is the smallest
            if(nums[mid]<nums[mid-1]) return nums[mid];

            if(nums[mid]>nums[0]) l = mid+1;// search to the right
            else r = mid; //search to the left
        }
        return nums[0];
    }
}
# @lc code=end