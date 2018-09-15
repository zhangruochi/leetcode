
/*
name   : zhangruochi
email  : zrc720@gmail.com
time   : 2018-09-15

problem info
-leetcode number: 1
-Description:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. 

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/

import java.io.*;
import java.util.*;

class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for(int i=0; i< nums.length-1; i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[j] == target - nums[i]){
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }   
        }
        return null;
    }


    public int[] twoSumImprove(int[] nums, int target){
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i =0; i<nums.length; i++){
            if(map.containsKey(target-nums[i]))
                return new int[]{map.get(target-nums[i]),i};
            map.put(nums[i],i);
        }
        return null;
    }

    public static void main(String[] args) {
        int[] input = {-1,-2,-3,-4,-5};
        int target = -8;
        TwoSum solution = new TwoSum();
        int[] result = solution.twoSumImprove(input,target);
        System.out.println(result[0] + " " + result[1]);     
    }


};
