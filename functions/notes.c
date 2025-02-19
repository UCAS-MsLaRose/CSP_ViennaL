// Vienna LaRose, Function notes in C
#include <stdio.h>
int num;
char name[50], place[50], verb[50];
int add(int numOne, int numTwo){
    return numOne+numTwo;
}
void due(char assignment[50], char day[20]){
    printf("The %s assignment is due %s\n", assignment, day);
}

int main(void){
    //printf("Please tell me a number:\n");
    //scanf("%d", num);
    //add(num,10);
    //add(8,1);
    //printf("%d",add(72,5));
    due("Functions Notes", "Today");
    due("Hello World Update", "Tomorrow");
    due("Fincancial Calulator Update", "Friday");
    return 0;
}