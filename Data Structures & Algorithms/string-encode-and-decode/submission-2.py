class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = ""
        for str in strs:
            str_len = len(str)
            encoded_str += f"{str_len}#" + str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            size = 0
            while s[i] != "#":
                size = size * 10 + int(s[i])
                i += 1
            i += 1
            end = i + size
            repair_str = s[i:end]
            i = end
            res.append(repair_str)
        return res