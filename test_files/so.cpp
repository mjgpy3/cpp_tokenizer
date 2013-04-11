#include <iostream>
#include <string>
using namespace std;

int main()
{
        string a, b,c = "New string";
        int num_1 = 5,num_2=12.0,result=0;
        string str1, str2 = "Paper, Coin and cosmic brownie";

        result=5;
        result&= 7;

        if (result == 5)
        {
        	result = num_2 % num_1;
                result ^= 5;
        }
        else if (result >= 9)
        {
        }

	cout << c << " is your value..." << endl;
	return 0;
}
