#
# @lc app=leetcode.cn id=1028 lang=java
#
# [1028] interval-list-intersections
#
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        //关键：双指针递进比较interval

         List<Integer[]> ans = new ArrayList<>();
        int i = 0, j = 0;
        int size = 0;
        

        while (i < A.length && j < B.length) {
            // 比较A[i] 交于 B[j],start为较大值，end为较小值
            int start = Math.max(A[i][0], B[j][0]);
            int end = Math.min(A[i][1], B[j][1]);
            if(start <= end) {
                ans.add(new Integer[2]);
                size++;
                ans.get(size-1)[0] = start;
                ans.get(size-1)[1] = end;
            }

            // 指针随着end递进
            if(A[i][1] < B[j][1]){
                i++;
            }else{
                j++;
            }

        }
        int[][] res = new int[size][2];
        for(int k =0;k<size;k++){
            res[k][0] = ans.get(k)[0];
            res[k][1] = ans.get(k)[1];
        }
        return res;
    }
}
# @lc code=end