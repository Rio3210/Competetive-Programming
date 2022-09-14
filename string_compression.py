class Solution(object):
    def compress(self, chars):
        i = 0
        base = 0
        while i < len(chars):
            c = chars[i]
            count = 0
            while i < len(chars) and chars[i] == c:
                i += 1
                count += 1
            chars[base] = c
            base += 1
            if count > 1:
                for n in list(str(count)):
                    chars[base] = n
                    base += 1
        return base
