class Solution(object):
    
    def decodeString(self, s):
        stack = []
        curr_str = ""
        curr_num = 0
        
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                # print(stack)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            else:
                curr_str += c
        return "".join(stack[::-1])+curr_str
                
        
#         length = len(s)
#         result = []
#         while i < length:
#             if s[i].isdigit():
#                 count_str = ''
#                 while s[i] != '[':
#                     count_str += s[i]
#                     i += 1
#                 count = int(count_str)
#                 i += 1
#                 i, substr = self.dfs(s, i)
#                 result.append(count * substr)
#             elif s[i] == ']':
#                 i += 1
#                 return i, ''.join(result)
#             else:
#                 result.append(s[i])
#                 i += 1

#         return ''.join(result)

#     def decodeString(self, s):
#         if not s or len(s) == 0:
#             return ''

#         return self.dfs(s, 0)