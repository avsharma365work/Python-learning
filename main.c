

#include <stdio.h>
//function prototyping
void factorial(int x);

int main(){
    factorial(5);
    
    
   return 0;
}
void factorial(int x){
    int r=1;
    //apply for loop
    for(int i = 1;i<=x;i++){
        r *=i;
        
    }
    printf("Factorial is = %d",r);
}

   

    




