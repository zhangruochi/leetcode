/*
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

*/

//把原数组中出现的数其应该所在的位置上置为负值，然后重新遍历如果大于0，则表示从未出现过

#include "vector"
#include "cmath"
#include "iostream"
using namespace std;


class Solution{
public:
    vector<int> findDisappearedNumbers(vector<int>& nums){
        for(int i=0;i<nums.size();i++){
            int m = abs(nums[i]) - 1;  //应该出现的位置
            nums[m] = nums[m] > 0 ? -nums[m] : nums[m];     
        }
            
        vector<int> result;
        for(int i=0;i<nums.size();i++){
            if(nums[i] > 0 )
                result.push_back(i+1);
        }

        return result;    
    }
};


int main(int argc, char const *argv[])
{
    Solution s;
    //int nums[] = {4,3,2,7,8,2,3,1};
    int nums[] = {1,2};
    vector<int> nums_vector(nums,nums+2);

    vector<int> result = s.findDisappearedNumbers(nums_vector);

    for(int i=0;i<result.size();i++){
        cout<<result[i]<<endl;
    }


    return 0;
}