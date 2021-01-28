#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;

    double root1, root2, discriminant;

    discriminant = b * b - 4 * a * c;

    if (a == 0 && b != 0) {
        cout << -c / b << endl;
    } else if (a != 0 and discriminant >= 0) {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);

        if (root1 == root2) {
            cout << root1 << endl;
        } else {
            cout << root1 << endl;
            cout << root2 << endl;
        }
    }
}
