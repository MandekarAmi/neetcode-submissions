class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ad =  {}
        for word in strs:
            root = "".join(sorted(word))
            if root in ad:
                ad[root].append(word)
            else:
                ad[root] = [word]

        op = []
        for key in ad:
            op.append(ad[key])
        
        return op
        