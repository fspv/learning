#include <iostream>
#include <vector>

using namespace std;

int main() {
    int num;
    cin >> num;

    vector<int> container = {};
    string result = "";

    while (num > 0) {
        container.push_back(num & 1);
        num = num >> 1;
    }

    for (int pos = container.size() - 1; pos >= 0; pos--) {
        result.append(to_string(container[pos]));
    }

    cout << result << endl;
}
