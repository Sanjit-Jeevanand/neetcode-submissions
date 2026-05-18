class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = {}
        ans = [] 
        count = -1
        for i in range(len(strs)):
            arr[i] = Counter(strs[i])
        for i in range(len(arr)):
            if arr[i] != 0:
                ans.append([strs[i]])
                count += 1
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j] and arr[j] != 0:
                    ans[count].append(strs[j])
                    arr[j] = 0
        return ans