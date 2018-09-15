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
    if(x == 0 || x == 1)
        return x;

    int left = 1, right = x/2;

    while(left <= right){

        int mid = (left + right)/2;
        //printf("%d,%d,%d\n",mid,left,right);

        if(x / mid == mid)
            return mid;

        else if(x / mid < mid )
            right = mid - 1;

        else if (x / mid > mid)
            left = mid + 1; 
    }

    return right;
}

//2147395600

int main(){
    printf("%d\n",mySqrt(1));
    return 0;
}