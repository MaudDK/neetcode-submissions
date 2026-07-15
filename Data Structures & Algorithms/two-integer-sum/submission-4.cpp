class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> prevMap;

        for(int i = 0; i < nums.size(); i++){
            int c = target - nums[i];
            if (prevMap.contains(c)){
                return {prevMap[c], i};
            }
            prevMap[nums[i]] = i;
        }
        return {};
        
    }
};
