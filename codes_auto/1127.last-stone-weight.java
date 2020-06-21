#
# @lc app=leetcode.cn id=1127 lang=java
#
# [1127] last-stone-weight
#
import java.util.PriorityQueue;
class Solution {
    // 【常规方法】注意默认是小根堆, 这题需要大根堆
    //【更快的方法】java的int[]排序是用的快排，所以重复利用Arrays.sort(stones)理论更慢，实际更快。
    // 关键：因为第一次快排之后，只改变一对逆序值，
    public int lastStoneWeight(int[] stones) {
        int end = stones.length - 1;
        int k = 0;
        while( k != stones.length && k != stones.length - 1 ){
            //重复利用Arrays.sort(stones)理论更慢，实际更快。
            Arrays.sort(stones);
            int x = stones[end - 1];
            int y = stones[end];
            if( x == y ){
                stones[end - 1] = stones[end] = -1;
                //利用转为-1再sort, end -= 2; 每次加入一对逆序
                k += 2;
            }else{
                stones[end - 1] = stones[end] - stones[end - 1];
                stones[end] = -1;
                k += 1;
            }
        }
        Arrays.sort(stones);
        //注意特判，纠正输出为-1的情况
        return k == stones.length ? 0 : stones[end];
    }
    /*
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1,o2)->o2-o1);
        for(int i : stones){
            pq.add(i);
        }
        while(pq.size()>1){
            int newStone = pq.poll()-pq.poll();
            if(newStone !=0 || pq.size() == 0){
                pq.add(newStone);
            } 
        }
        return pq.poll();
    }*/
}
# @lc code=end