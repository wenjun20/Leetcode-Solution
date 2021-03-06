// Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
//
//  
//
//
// Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
//
//  
//
//
// The largest rectangle is shown in the shaded area, which has area = 10 unit.
//
//  
//
// Example:
//
//
// Input: [2,1,5,6,2,3]
// Output: 10
//
//
//  
// Example 1:
//
//
// Input: heights = [2,1,5,6,2,3]
// Output: 10
// Explanation: The above is a histogram where width of each bar is 1.
// The largest rectangle is shown in the red area, which has an area = 10 units.
//
//
// Example 2:
//
//
// Input: heights = [2,4]
// Output: 4
//
//
//  
// Constraints:
//
//
// 	1 <= heights.length <= 105
// 	0 <= heights[i] <= 104
//
//


class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<int> stk; 
        heights.push_back(0);
        int ans = 0; 
        for (int i = 0; i < heights.size(); i++){
            int last = i, origin = heights[i];
            while (stk.size() && heights[i] < heights[stk.back()]){
                ans = max(ans, (i - stk.back())*heights[stk.back()]);
                last = stk.back();
                stk.pop_back();
            }
            heights[last] = origin;
            stk.push_back(last);
        }
        return ans;
    }
};
