class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(s, opening, closing):
            if len(s) == 2 * n:
                ans.append(s)  
                return
            if opening < n:
                helper(s + '(', opening + 1, closing)
            if closing < opening:
                helper(s + ')', opening, closing + 1)
        helper('', 0, 0)
        return ans



