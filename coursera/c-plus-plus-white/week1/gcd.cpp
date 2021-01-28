#include <iostream>

using namespace std;

int main() {
    int left, right, tmp;

    cin >> left;
    cin >> right;

    while (right != 0) {
        tmp = right;
        right = left % right;
        left = tmp;
    }

    cout << left << endl;
}
