
/*
name   : zhangruochi
email  : zrc720@gmail.com
time   : 2018-09-15

problem info
-leetcode number:   13
-description: 

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

*/

import java.util.*;

class RomanToInteger {
    public static int romanToInt(String s) {
       HashMap<Character,Integer> map = new HashMap<Character,Integer>();
       map.put('I',1);
       map.put('V',5);
       map.put('X',10);
       map.put('L',50);
       map.put('C',100);
       map.put('D',500);
       map.put('M',1000);

       int result = 0;

       for(int i=0;i<s.length()-1;i++){
        if(map.get(s.charAt(i)) < map.get(s.charAt(i+1)))
            result += (-map.get(s.charAt(i)));
        else
            result += map.get(s.charAt(i));
       }
       result += map.get(s.charAt(s.length()-1));

       return result;
    }

    public static void main(String[] args) {
        System.out.println(RomanToInteger.romanToInt("III"));
    }




};
