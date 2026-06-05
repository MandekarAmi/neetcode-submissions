class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(c for c in s if c.isalnum()).lower()
        l = len(new_s)
        if l%2 == 0:
            l, r = new_s[:l//2], new_s[l//2:]
        else:
            l, r = new_s[:l//2], new_s[l//2+1:]

        print(l)
        print(r)
        
        i,j = 0, len(r)-1
        while i < len(l):
            if l[i] != r[j]:
                return False
            i, j = i+1, j-1
        return True
        