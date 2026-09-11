class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map = {}

        for x in range(len(s)):
            map[s[x]] = map.get(s[x],0) + 1
            map[t[x]] = map.get(t[x],0) - 1
        
        return all(v == 0 for v in map.values())
