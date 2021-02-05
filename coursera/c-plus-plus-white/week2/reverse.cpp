#include <iostream>
#include <vector>

using namespace std;

void Reverse(vector<int>& toReverse) {
  int left = 0;
  int right = toReverse.size() - 1;
  int tmp;

  while (left < right) {
    tmp = toReverse[left];
    toReverse[left] = toReverse[right];
    toReverse[right] = tmp;
    left++;
    right--;
  }
}
