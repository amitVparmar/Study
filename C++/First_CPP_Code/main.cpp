//This brings IOSTREAM library
#include <iostream>

consteval int get_value(){
    return 3;
}
//Main function is the entry point of the program
int main(){
    std::cout << "Hello World!" << std::endl;
    std::cout << get_value();
    return 0;
}