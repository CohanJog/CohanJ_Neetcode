class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set = {}
        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in set:
                set[x].append(strs[i])

            else:
                set[x] = [(strs[i])]

        return list(set.values())   