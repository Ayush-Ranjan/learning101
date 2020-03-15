#include <stdio.h>
#include <iostream>
void update(int *a,int *b) {
    int c=*a+*b;
    int d=(*a>*b?-1:1)*(*b-*a);
    *a=c;
    *b=d;
    // Complete this function    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}