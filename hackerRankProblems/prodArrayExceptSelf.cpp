# 7/1/2022

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer(nums.size(), 0);
        vector<int> leftSide(nums.size(), 0);
        vector<int> rightSide(nums.size(), 0);
        
        for (int i=0; i<nums.size(); i++){
            if(i==0) leftSide[i] = nums[0];
            leftSide[i] = nums[i] * leftSide[i-1];
        }
        
        for (int i = nums.size() -1; i >=0; i--){
            if(i==nums.size()-1) rightSide[nums.size()-1] = nums[nums.size()-1];
            rightSide[i] = nums[i] * rightSide[i+1];
        }
        
        if (nums.size() > 1){
            answer[0] = rightSide[1];
            answer[nums.size()-1] = leftSide[nums.size()-2];
        }
        
        for (int i=1; i< nums.size()-1; i++){
            answer[i] = leftSide[i-1] * rightSide[i+1];
        }
        
        return answer;
    }
};
