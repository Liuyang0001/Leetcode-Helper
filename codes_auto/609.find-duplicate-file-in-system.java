#
# @lc app=leetcode.cn id=609 lang=java
#
# [609] find-duplicate-file-in-system
#
class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
    // use content as key, list of filenames as value
    HashMap < String, List> map = new HashMap < > ();
        for (String path: paths) {
            String[] values = path.split(" ");
            for (int i = 1; i < values.length; i++) {
                String[] name_content = values[i].split("\\(");
                String content = name_content[1].replace(")", "");
                if(!map.containsKey(content)) map.put(content, new ArrayList());
                map.get(content).add(values[0] + "/" + name_content[0]);
            }
        }
        List < List < String >> res = new ArrayList < > ();
        for (String key: map.keySet()) {
            if (map.get(key).size() > 1)
                res.add(map.get(key));
        }
        return res;
    }
}
# @lc code=end