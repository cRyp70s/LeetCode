class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        real_anagrams = []
        strs.sort()
        for i in strs:
            b = sorted(i)
            for j in range(len(anagrams)):
                if anagrams[j] == b:
                    real_anagrams[j].append(i)
                    break
            else:
                anagrams.append(b)
                real_anagrams.append([i])
        return real_anagrams
