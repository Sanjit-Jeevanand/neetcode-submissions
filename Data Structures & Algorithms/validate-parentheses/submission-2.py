class Solution:
    def isValid(self, s: str) -> bool:
        opp = {"]": "[", "}": "{", ")": "("}
        st = []
        for i in s:
            if i in opp:
                if st and opp[i] != st[-1]:
                    return False
                if st:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return False if st else True