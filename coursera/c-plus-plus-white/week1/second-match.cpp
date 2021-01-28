#include <iostream>
#include <string>

using namespace std;

int main() {
    char target = 'f';
    bool seen = false;

    string input;

    cin >> input;

    for (int pos = 0; pos < input.size(); pos++) {
        if (input[pos] == target) {
            if (seen) {
                cout << pos << endl;
                return 0;
            } else {
                seen = true;
            }
        }
    }

    if (seen) {
        cout << -1 << endl;
    } else {
        cout << -2 << endl;
    }
}
