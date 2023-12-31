// Sum Square Difference

#include <iostream>

using namespace std;

int main()
{
    int squares = 0, sum = 0;

    for (int i = 1; i <= 100; i++)
        squares += i * i;

    for (int i = 1; i <= 100; i++)
        sum += i;
    
    cout << sum * sum - squares;
}
