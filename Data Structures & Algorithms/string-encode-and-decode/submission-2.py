class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res += str(len(c)) + "-" + c
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "-":
                j+=1
            # print(s[i:j])
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            # print(i,j,length)
            # print(s[i+2:i+length+2])
            # print(s[j+1:j+length+1])
            i=length+j+1
        return res
