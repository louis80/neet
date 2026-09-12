class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: 
            return []
        
        anagrams = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]

        return list(anagrams.values())