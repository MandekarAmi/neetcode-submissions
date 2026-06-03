class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ad =  {}
        for word in strs:
            freq_arr = self.create_freq_arr(word)
            if freq_arr in ad:
                ad[freq_arr].append(word)
            else:
                ad[freq_arr] = [word]
        
        return list(ad.values())

    def create_freq_arr(self, word):
        freq_arr = [0]* 26
        for c in word:
            freq_arr[ord(c)-ord('a')] = freq_arr[ord(c)-ord('a')] + 1
        return "".join(str(freq_arr))
        