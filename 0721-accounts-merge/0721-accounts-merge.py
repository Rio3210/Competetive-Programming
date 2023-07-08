class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        
        def find(s):
            if s not in parent:
                parent[s]=s
            while s!=parent[s]:
                parent[s]=parent[parent[s]]
                s=parent[s]
            return s
        
        def union(u,v):
            parent[find(u)]=find(v)
                
      
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                union(account[1], email)

        # print(parent)
        merged_acc = defaultdict(list)
        for email in parent:
            merged_acc[find(email)].append(email)
        print(merged_acc)
        
        ans = []
        for emails in merged_acc.values():
            name = email_to_name[emails[0]]
            ans.append([name] + sorted(emails))
        
        return ans
        