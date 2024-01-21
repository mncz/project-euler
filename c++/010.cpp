// Summation of Primes

#include <iostream>

using namespace std;

int isPrime(int number)
{
    if (number <= 1)
        return false;
    
    for (int i = 2; i <= number / 2; i++)
        if (number % i == 0)
            return false;
    
    return true;
}

int main()
{
    long sum = 0;

    for (int i = 0; i < 2000000; i++)
    {
        if (isPrime(i))
            sum += i;
    }

    cout << sum;
}
