#
# @lc app=leetcode.cn id=1039 lang=java
#
# [1039] find-the-town-judge
#
class Solution {
    public int findJudge(int N, int[][] trust) {
        //【关键】所有人都信任法官，说明法官的入度为N-1
        int[] inDegree = new int[N];
        for(int[] pair: trust){
            inDegree[pair[0]-1]--;
            inDegree[pair[1]-1]++;
        }
        for(int i=0; i<N; i++){
            if(inDegree[i] == N-1){
                return i+1;
            }
        }
        return -1;

    }
}
# @lc code=end