class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            encoding = [0] * 26
            for c in word:
                encoding[ord(c) - ord('a')] +=1
            anagrams[tuple(encoding)].append(word)
        
        return list(anagrams.values())

        