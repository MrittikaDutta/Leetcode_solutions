class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]
        bad = set()
        for u,v in friendships:
            u-=1; v-=1
            if langs[u] & langs[v]: 
                continue
            bad.add(u)
            bad.add(v)
        if not bad:
            return 0
        ans = float('inf')
        for l in range(1,n+1):
            cnt = 0
            for u in bad:
                if l not in langs[u]:
                    cnt+=1
            ans = min(ans,cnt)
        return ans
