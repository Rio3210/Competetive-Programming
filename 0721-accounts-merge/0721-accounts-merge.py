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
        merged_accounts = defaultdict(list)
        for email in parent:
            merged_accounts[find(email)].append(email)
        # print(merged_accounts)
        
        ans = []
        for emails in merged_accounts.values():
            name = email_to_name[emails[0]]
            ans.append([name] + sorted(emails))
        
        return ans
        