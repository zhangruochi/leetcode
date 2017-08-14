/*

Implement int sqrt(int x).

Compute and return the square root of x.


*/

#include "stdio.h"

int mySqrt_me(int x) {

    if( x == 1 || x == 0)
        return x;

    int i =0;
    for(; i<= x/2; i++){

        if((i*i) > x || (i * i) < 0)
            break;
    }

    return i - 1;

}

//采用二分法
int mySqrt(int x){
    if(x == 0)
        return 0;

    int left = 1, right = x/2;

    while(left < right){
        int mid = left + (right - left)/2;

        if(x / mid > left )
            left = mid;

        if(x / mid < right)
            right = mid;
    }

    return left - 1;



}
//2147395600

int main(){
    printf("%d\n",mySqrt(9));
    return 0;
}