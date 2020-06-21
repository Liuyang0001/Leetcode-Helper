#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] validate-ip-address
#
class Solution:
    def validIPAddress(self, IP: str) -> str:
        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        IPv4Address = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')

        chunk_IPv6 = r'([0-9a-fA-F]){1,4}'   # 1 to 4 use comma
        IPv6Address = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

        if IPv4Address.match(IP):
            return 'IPv4'
        elif IPv6Address.match(IP):
            return 'IPv6'
        else:
            return 'Neither'

# @lc code=end