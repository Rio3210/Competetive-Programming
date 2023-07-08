class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent={}
        
        def find(x):
            if x not in parent:
                parent[x]=x
            
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        
        def union(x,y):
            parent_x=find(x)
            parent_y=find(y)
            
            if parent_x>parent_y:
                parent[parent_x]=parent_y
            else:
                parent[parent_y]=parent_x
        
        for i in equations:
            if i[1]=="=":
                union(i[0],i[3])

        for i in equations:
            if i[1]=="!":
                if find(i[0])==find(i[3]):
                    return False

        return True