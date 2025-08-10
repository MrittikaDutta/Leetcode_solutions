class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        l=len(f)
        f.append(0)
        k=0
        if f[0]==0 and f[1]==0:
            f[0]=1
            k+=1
        for i in range(1,l):
            if f[i]==0 and f[i-1]==0 and f[i+1]==0:
                k+=1
                f[i]=1
        if k>=n:
            return True
        return False
