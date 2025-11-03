class Solution {
public:
    bool simulate(vector<int> nums, int i, int d) {
        int n = nums.size();
        while (i >= 0 && i < n) {
            if (nums[i] == 0) {
                i += d;
            } else {
                nums[i]--;
                d *= -1;
                i += d;
            }
        }
        for (int x : nums)
            if (x != 0) return false;
        return true;
    }

    int countValidSelections(vector<int>& nums) {
        int res = 0, n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                if (simulate(nums, i, 1)) res++;
                if (simulate(nums, i, -1)) res++;
            }
        }
        return res;
    }
};
