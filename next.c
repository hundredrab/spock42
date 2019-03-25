#include<stdio.h>

int IsPrime(int number)
{

    if (number == 2 || number == 3)
        return 1;

    if (number % 2 == 0 || number % 3 == 0)
        return 0;

    int divisor = 6;
    while (divisor * divisor - 2 * divisor + 1 <= number)
    {

        if (number % (divisor - 1) == 0)
            return 0;

        if (number % (divisor + 1) == 0)
            return 0;

        divisor += 6;

    }

    return 1;

}

int NextPrime(int a)
{

    while (!IsPrime(++a)) 
    {
    }
    return a;

}

void main(){
    int a;
    scanf("%d", &a);
    printf("%d\n", NextPrime(a) - a);
}
