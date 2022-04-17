class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:
            key = ''.join(sorted(str))

            try:
                group[key].append(str)
            except KeyError:
                group[key] = [str]

        return sorted(group.values(), key=lambda x: len(x))
