#
# @lc app=leetcode.cn id=56 lang=java
#
# [56] merge-intervals
#
class Solution {
    public int[][] merge(int[][] intervals) {
        //关键：用Interval概念, 按start排序之后，merge就是遍历interval,比较start尝试延伸end。
        Arrays.sort(intervals,Comparator.comparingInt(interval ->interval[0]));
        LinkedList<int[]> merged = new LinkedList<>();
        for (int i = 0; i < intervals.length; i++) {
            //如果已合并区间为0，或当前区间的start大于前面区间的end而没有需要合并的部分。
            if(merged.isEmpty() || intervals[i][0]> merged.getLast()[1])
                merged.add(intervals[i]);
            //合并其实就是【比较后】尝试延长最后一个加入的区间的end
            else 
                merged.getLast()[1] = Math.max( merged.getLast()[1], intervals[i][1]);
        }
        return merged.toArray(new int[merged.size()][2]);
       

            
            
        
    }
}
# @lc code=end