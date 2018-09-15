
/*
name   : zhangruochi
email  : zrc720@gmail.com
time   : 2018-09-15

problem info
-leetcode number: 14
-description: 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

*/


class LongestCommonPrefix {

    public static int minLength(String[] strs){
        if(strs.length == 0)
            return 0;
        int min = strs[0].length();
        for(String str : strs){
            if(str.length()<min)
                min = str.length();
        }
        return min;
    }

    public static String longestCommonPrefix(String[] strs) {
        StringBuffer result = new StringBuffer();
        int min = minLength(strs);
        //System.out.println(min);

        for(int i=0;i<min;i++){
            char c = strs[0].charAt(i);
            //System.out.println(c);
            for(String str : strs){
                if(str.charAt(i) != c)
                    return result.toString();
            }
            result.append(c);    
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String[] strs = {"fl","flow","flight"};
        System.out.println(LongestCommonPrefix.longestCommonPrefix(strs)); 

    }
};
