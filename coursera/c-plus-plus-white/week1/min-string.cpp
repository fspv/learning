#include <iostream>
#include <string>

using namespace std;

int main() {
    string minString;
    string x, y, z;

    cin >> x;
    cin >> y;
    cin >> z;

    minString = x;

    if (y < minString) {
        minString = y;
    }

    if (z < minString) {
        minString = z;
    }

    cout << minString << endl;
}
