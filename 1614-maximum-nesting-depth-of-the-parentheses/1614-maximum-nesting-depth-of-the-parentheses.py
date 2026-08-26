class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth=0
        cur_depth=0
        res=[]
        for brac in s:
            if brac=='(':
                cur_depth+=1
                max_depth=max(cur_depth,max_depth)
            elif brac==')':
                cur_depth-=1
           
        return max_depth        