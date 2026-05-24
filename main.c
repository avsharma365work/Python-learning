//making atm machine software

#include <stdio.h>


int main(){

    int choice; int pin = 12300; int p; float cash = 0; float amt;
    while(1){
        //print options = menu
        printf("==========Welcome to Money Bank ATM==========\n");
        printf("(1) Pin Login\n");
        printf("(2) Cash Deposit\n");
        printf("(3) Cash Widhrawal\n");
        printf("(4) Balance Enquiry\n");
        printf("(5) Exit\n");
        //user choice
        printf("Enter your choice(1-4): "); scanf("%d",&choice);
        //main starting
        if(choice == 1){
            printf("Enter your Pin: "); scanf("%d",&p);
            if(pin == p){
                printf("Now, You login \n How can I help you\n");
            }
            else{
                printf("Wrong Pin");
                break;
            }
        }
        else if(choice == 2){
            printf("=====Cash deposit=====\n");
            printf("Enter deposit amount: "); scanf("%f",&amt);
            cash += amt;
            printf("You are deposit Rs\n %f",amt);
            printf("Thank you \n");
        }
        else if(choice == 3){
            printf("=====Cash Withdrawl===== \n");
            printf("Enter Withdraw amount: "); scanf("%f",&amt);
            cash -= amt;
            printf("You are Withdraw amt Rs %f \n",amt);
            printf("Thank you \n");

        }
        else if(choice == 4){
            printf("Your Current Balance is Rs %f",cash);

        }
        else if(choice == 5){
            printf("Exiting.....\n");
            printf("Thank you\n");
            break;
        }


    }


   return 0;
}

   

    




