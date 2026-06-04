class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        char_ls = ""
        for s in strs:
            char_ls = char_ls + str(len(s)) + ","
            encoded_str = encoded_str + s
        return char_ls + "#" + encoded_str


    def decode(self, s: str) -> List[str]:
        print("input - "+ s)
        num_arr_s = ""
        i=0
        num_arr_s = s.split("#", maxsplit=1)
        num_arr = num_arr_s[0].split(",")
        res = []
        for num in num_arr[:-1]:
            sub_s = num_arr_s[1][i:i+int(num)]
            res.append(sub_s)
            i = i+int(num)
        return res
        

        