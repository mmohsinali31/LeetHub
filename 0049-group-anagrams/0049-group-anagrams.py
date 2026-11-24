class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            freq = {}

            for char in word:
                freq[char] = freq.get(char, 0) + 1

            key = tuple(sorted(freq.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())