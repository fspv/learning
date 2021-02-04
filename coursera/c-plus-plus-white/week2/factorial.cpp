#include <iostream>

using namespace std;

int Factorial(int number) {
  if (number <= 0) {
    return 1;
  }

  return Factorial(number - 1) * number;
}

int main() {
  cout << Factorial(10) << endl;
  cout << Factorial(0) << endl;
  cout << Factorial(-1) << endl;

  return 0;
}
