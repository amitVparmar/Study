//This brings IOSTREAM library
#include <iostream>

int get_value(){
    return 3;
}
//Main function is the entry point of the program
int main(){
    std::cout << "Hello World!" << std::endl
    ; //semi-colon can be anywhere between 2 code lines
    std::cout << get_value(); //without endl

    //runtime error
    //int i = 7/0;
    //std::cout << "value : " << i << std::endl; //Error message : Floating point exception (core dumped)

    return 0;
}