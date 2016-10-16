#include <stdio.h>
int main(){

        int c = 0;
        int b = -1 ;
        int words = 0, lines =0;
        while( (c = getchar()) !=EOF){

            if( (c ==' ' || c =='\t' || c =='\n') && (b!=' ' && b != '\t' && b!='\n' ) )
            {
                    ++words;
            }
            else
            {
                    
            }

            if(c == '\n')
            {
                    ++lines;
            }
            b = c;
                

        }
        printf("%d , %d" ,words , lines);

}
