class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        st = set()
        n = len(s)
        for i in range(n):
            while s[i] in st and l < i:
                st.remove(s[l])
                l +=1 
            ans = max(ans,len(st)+1)
            st.add(s[i])
        return ans