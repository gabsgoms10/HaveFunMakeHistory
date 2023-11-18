#include<stdio.h>

int main(int argc, char const *argv[])
{
  /* Variables are allocated space in memory to store a variable
     Reffering to a variable name gets it's value
     Than the variable will behave as it is the value it has
     We have to declare the variable type*/
    
    int y;
    y = 34; // Integer
    float x = 4.05; // Floating point
    char grade = 'C';  // Single character
    char name[] = "Gabe"; //Array of characters

    printf("You have %d years old\n", y);
    printf("Hello %s\n", name);
    printf("Your average grade is %c\n", grade);
    printf("Your gpa is %f", x);
    // %d for int
    // %s for char array 
    // %c for char
    // %f for float
    return 0;
}