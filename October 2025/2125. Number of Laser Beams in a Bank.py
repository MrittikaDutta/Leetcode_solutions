class Solution {
public:
    int cnt,ls,ans;
    int numberOfBeams(vector<string>& bank) {
        for(auto &s:bank){
            for(auto i:s)cnt+= i=='1';
            if(cnt){
                ans+= ls*cnt;
                ls = cnt, cnt = 0;
            }
        }
        return ans;
    }
};
