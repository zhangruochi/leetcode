/*

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

*/

#include "iostream"
#include "vector"

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        //cout<<low<<","<<high<<endl;  
        
        while(low <= high){
            int mid = (low + high) / 2;
            
            if(nums[mid] == target)
                return mid;
            
            else if (nums[mid] < target)
                low = mid + 1;
            
            else
                high = mid - 1;
        }

        return low;
    }
};

int main(){

    int v1[1] = {1};
    vector<int> nums;
    for(int i = 0; i<1; i++){
        nums.push_back(v1[i]);
    }

    Solution solution;

    cout<< solution.searchInsert(nums,2)<< endl;


}



