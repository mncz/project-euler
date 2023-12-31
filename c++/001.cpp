// Multiples of 3 or 5

#include <iostream>

using namespace std;

int main()
{
    int i = 0, sum = 0;

    do
    {
        if (i % 3 == 0 || i % 5 == 0)
            sum += i;

        i += 1;
    } while (i < 1000);
    
    cout << sum;
}
