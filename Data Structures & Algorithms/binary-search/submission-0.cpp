class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int middleIndex = (left + right) / 2;
            int middle = nums[middleIndex];


            if (target == middle) {
                return middleIndex;
            }
            else if (target < middle) {
                right = middleIndex - 1;
            }
            else {
                left = middleIndex + 1;
            }
        }
        
        return -1;
    }
};
