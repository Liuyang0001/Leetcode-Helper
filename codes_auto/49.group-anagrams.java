#
# @lc app=leetcode.cn id=49 lang=java
#
# [49] group-anagrams
#
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList();
        Map<String, List> ans = new HashMap<String, List>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);
           if (!ans.containsKey(key)) ans.put(key, new ArrayList());
           //【注意】add返回boolean,故只能调用add来添加，而不能用add返回的结果来更新value.
            ans.get(key).add(s);

        }
        return new ArrayList(ans.values());
    }
}

# @lc code=end