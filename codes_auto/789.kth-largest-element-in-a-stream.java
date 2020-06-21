#
# @lc app=leetcode.cn id=789 lang=java
#
# [789] kth-largest-element-in-a-stream
#
class KthLargest {
    //关键：找K largest就是不断丢掉min保留K个largest,所以用默认的minHeap, construct是NlgK
    //【方法二】：constructor用quick select, 参照973，可以降低到平均O（N)，然后add是O（lgK）
    private PriorityQueue<Integer> pq;
    private int limit;

    public KthLargest(int k, int[] nums) {
        limit = k;
        pq = new PriorityQueue<>(k);
        for (int num : nums) {//O(nlgK)
             pq.add(num);
             if(pq.size()>k){//维护size=K, 等同python的heapq.pushpop(self.nums, val)
                 pq.poll();
             }
        } 
    }

    public int add(int val) {
        if (pq.size() < limit) {
            pq.add(val);
        } else if(val > pq.peek()){
            pq.poll();
            pq.add(val);
        }
        return pq.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
# @lc code=end