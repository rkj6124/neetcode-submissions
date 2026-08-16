class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False
        sonefreq = [0] * 26
        stwofreq = [0] * 26

        for i in range(l1):
            sonefreq[ord(s1[i]) - 97] += 1
            stwofreq[ord(s2[i]) - 97] += 1

        if sonefreq == stwofreq:
            return True

        for i in range(l1, l2):
            stwofreq[ord(s2[i]) - 97] += 1
            stwofreq[ord(s2[i-l1]) - 97] -= 1

            if sonefreq == stwofreq:
                return True
        return False