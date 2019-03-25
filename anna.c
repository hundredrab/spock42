#include<stdio.h>
#include<string.h>
#define min(x, y) (((x) < (y)) ? (x) : (y))

void main(){
        char a[100], b[100];
        scanf("%s", a);
        scanf("%s", b);
        
        int A[26],B[26],i;
        for(i=0 ; i< 26 ; i++)
        {    A[i] = 0;
            B[i] = 0;
        }
        for(i = 0 ; i< strlen(a); i++)
            A[(int)(a[i] - 'a')]++;
        for(i = 0 ; i< strlen(b) ; i++)
            B[(int)(b[i] - 'a')]++;
        int outp = 0;
        for(i=0 ; i< 26 ; i++)
        {
            outp = outp + A[i] + B[i] - 2*min(A[i],B[i]);
        }
        printf("%d\n", outp);
}

