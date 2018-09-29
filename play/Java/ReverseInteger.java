
/*
name   : zhangruochi
email  : zrc720@gmail.com
time   : 2018-09-15

problem info
-leetcode number:  7  
-description: 

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

*/


class ReverseInteger {
        

    public static int reverse(int x) {
        int xOriginal = x;
        int quotient,remainder, tmp; 
        int result = 0;

        while(x!=0){
            quotient = x/10;
            remainder = x%10;
        
            tmp = result*10 + remainder;
            if((tmp-remainder)/10 != result)
                return 0;

            result = tmp;
            x = quotient;
        }


        return result;
                    
    }

    public static void main(String[] args) {
        int x = 1534236469;
        int y = -123;
        System.out.println(ReverseInteger.reverse(y));


    }

};
