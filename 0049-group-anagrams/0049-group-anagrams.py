class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}

        for char in strs:
            print(char)
            key = "".join(sorted(char))
            result.setdefault(key,[])
            result[key].append(char)

        return list(result.values())

                