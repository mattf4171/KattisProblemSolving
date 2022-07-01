# 7/1/2022
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> runningSum;
        for (int i=0; i< nums.size(); i++){
            if (i == 0){
                runningSum.push_back(nums[i]);
            }else{
                runningSum.push_back(runningSum[i-1] + nums[i]);
            }
        }
    return runningSum;
    }
};
