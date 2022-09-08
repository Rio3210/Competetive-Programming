class Solution(object):
    def dfs(self, s, i):
        length = len(s)
        result = []
        while i < length:
            if s[i].isdigit():
                count_str = ''
                while s[i] != '[':
                    count_str += s[i]
                    i += 1
                count = int(count_str)
                i += 1
                i, substr = self.dfs(s, i)
                result.append(count * substr)
            elif s[i] == ']':
                i += 1
                return i, ''.join(result)
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)

    def decodeString(self, s):
        if not s or len(s) == 0:
            return ''

        return self.dfs(s, 0)
