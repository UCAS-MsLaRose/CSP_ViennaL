// Vienna LaRose, Loops notes in C
#include <stdio.h>

int main(void){
    // 1. What is a loop? 
        //a section of code repeated multiple time

    // 2. What are the two types of loops?
        //While Loops
        int start = 0;
        while(start < 5){
            printf("Hello!\n");
            start++;
        }
        //For Loops
        int q;
        for(q=0;q<5;q++){
            printf("%d\n", q);
        }
    // 3. What is iteration
        //repeating something with minor changes each time

    // 4. What are arrays(list)? 
        // An array is a variable holding multiple values

    // 8. How do you make arrays(lists) in C?
        //Array items must all be the same data type!
    int grades[] = {88, 97, 100, 70, 72, 99, 61};
        // 1. set data type 2. AFTER naming put brackets and write the length of the list 3. List is surrounded by curly brackets {} 4. Commas , between each item
    // print a single item from a list
    printf("CSP Grade: %d\n", grades[2]);
    // Change an item in the array
    grades[2] = 95;
    printf("CSP Grade: %d\n", grades[2]);
    // Size of array(list) in bytes
    int size = sizeof(grades);
    // length in arrays(list) items
    int length = sizeof(grades)/sizeof(grades[0]);
    printf("The array is %d items long.\n", length);
    // array with strings
    //First brackets sets length of array(list)
    //Second brackets sets length of each string
    char movies[][20] = {"Cars", "Treasure Planet", "An American Tale", "Marley and Me", "The Avengers"};
    printf("The movie is %s!\n", movies[1]);

    int mlength = sizeof(movies)/sizeof(movies[0]);
    // 9. How do you make for loops in C?
    // set the iterator, keeps track of times through the loop (best practice to set as x or i)
    int x;
    // in parens (starting point; ending point; count by)
    for(x=0;x<=10;x+=2){
        printf("%d\n", x);
    }
    int m;
    for(m=0;m<mlength;m++){
        printf("%s\n", movies[m]);
    }
    // 10. How do you make while loops in C?
    int w = 100;//start point

    while(w>=0){//stop point
        printf("%d\n", w);
        w -= 10;//What we count by
    }

    return 0;
}