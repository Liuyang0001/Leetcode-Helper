#
# @lc app=leetcode.cn id=242 lang=java
#
# [242] valid-anagram
#
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) alphabet[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) alphabet[t.charAt(i) - 'a']--;
        for (int i : alphabet){
            if (i != 0) {
                return false;
            }
        } 
        return true;
    }
}
# @lc code=end