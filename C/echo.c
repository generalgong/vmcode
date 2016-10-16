#include <stdio.h>
#include<stdlib.h>
int main(){

        int c = 0;
        int b = -1 ;
        while( (c = getchar()) !=EOF){

            if( (c ==' ' || c =='\t') && (b==' '|| b == '\t') )
            {
            }
            else
            {
                    putchar(c);
            }
            b = c;
                

        }
}
