#
# @lc app=leetcode.cn id=860 lang=java
#
# [860] design-circular-queue
#
class MyCircularQueue {
    // FIFO,当队首元素出队时，产生空位，为了继续在队尾加入元素填补，使用一维【数组】模拟环形队列
    int[] queue;
    int head;
    int size;
    int CAPACITY;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        queue = new int[k];
        head =0;
        size =0;
        CAPACITY = k;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if(size == CAPACITY) return false;
        
        queue[(head+size)%CAPACITY]=value;
        size++;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        // deletion会将head的位置后移
        if(size == 0) return false;
        head++;
        size--;
        if(head == CAPACITY) head =0;
        return true;
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        //特判
        if(size ==0) return -1;
        return queue[head];
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if(size ==0) return -1;
        return queue[(head+size-1)%CAPACITY];
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return size == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return size == CAPACITY;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
# @lc code=end