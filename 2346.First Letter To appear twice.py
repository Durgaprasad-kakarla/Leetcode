class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_order = []
        ctr = {}
        for c in s:
            if c in ctr:
              ctr[c] += 1
              if ctr[c]==2:
                return c
            else:
              ctr[c] = 1
