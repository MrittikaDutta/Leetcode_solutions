class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[]
        for i in folder:
            if not res or not i.startswith(res[-1] + '/'):
                res.append(i)
        return res
