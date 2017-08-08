#include "iostream"

using namespace std;


class Solution {

public:
    int reverse(int x){
        cout<< x << endl;
        
        const int MIN = 0x80000000;
        const int MAX = 0x7fffffff;

        long long sum = 0;
        int remainder = 0;

        while(x != 0){
            remainder = x % 10;
            x = x / 10;

            sum = sum * 10 + remainder;

            if(sum > MAX || sum < MIN)
                return 0;
        }

        return sum;
    }
    
};


int main(){
    Solution solution;
    int result;

    result = solution.reverse(1534236469);
    cout << result << endl;
}



