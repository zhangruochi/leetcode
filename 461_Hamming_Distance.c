/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2 31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?

The above arrows point to positions where the corresponding bits are different.
*/

#include "stdio.h"

int hammingDistance(int x, int y) {
    int tmp = x ^ y;
    int counter = 0;
    int mask = 1,flag = sizeof(int) * 8;
 
    while(flag > 0){
        if(tmp & mask)
            counter ++;
        mask = mask << 1;
        flag --;
    }

    return counter;

}


int main(int argc, char const *argv[])
{
    printf("%d\n",hammingDistance(93,73));
    return 0;
}
