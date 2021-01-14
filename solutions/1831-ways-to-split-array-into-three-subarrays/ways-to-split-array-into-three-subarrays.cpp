// A split of an integer array is good if:
//
//
// 	The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
// 	The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
//
//
// Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.
//
//  
// Example 1:
//
//
// Input: nums = [1,1,1]
// Output: 1
// Explanation: The only good way to split nums is [1] [1] [1].
//
// Example 2:
//
//
// Input: nums = [1,2,2,2,5,0]
// Output: 3
// Explanation: There are three good ways of splitting nums:
// [1] [2] [2,2,5,0]
// [1] [2,2] [2,5,0]
// [1,2] [2,2] [5,0]
//
//
// Example 3:
//
//
// Input: nums = [3,2,1]
// Output: 0
// Explanation: There is no good way to split nums.
//
//  
// Constraints:
//
//
// 	3 <= nums.length <= 105
// 	0 <= nums[i] <= 104
//


class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        const int mod = 1e9 + 7, n = nums.size(); 
        vector<int> prefix(n + 1); 
        for (int i = 1; i <= n; i++){
            prefix[i] = prefix[i - 1] + nums[i - 1]; 
        }
        int ans = 0; 
        auto beg = next(prefix.begin(), 2); 
        for (int i = 1; i < n - 1; i++, beg = next(beg)){
            int s = prefix[i]; 
            auto it_l = lower_bound(beg, prefix.end(), 2*s);
            auto it_r = upper_bound(beg, prev(prefix.end()), (prefix.back() - s) / 2 + s);
            ans += max((int)(it_r - it_l), 0);
            ans %= mod;
        }
        return ans;
    }
};

