#include <iostream>
#include <vector>
#include <string>

using namespace std;

void ReverseVector(vector<string>& toReverse) {
  int left = 0;
  int right = toReverse.size() - 1;
  string tmp;

  while (left < right) {
    tmp = toReverse[left];
    toReverse[left] = toReverse[right];
    toReverse[right] = tmp;
    left++;
    right--;
  }
}

void MoveStrings(vector<string>& source, vector<string>& destination) {
  string tmp;
  ReverseVector(source);  // Inefficiend, just for practice purposes
  while (!source.empty()) {
    tmp = source[source.size() - 1];
    source.pop_back();
    destination.push_back(tmp);
  }
}

int main() {
  vector<string> source = {"a", "b", "c"};
  vector<string> destination = {"z"};

  MoveStrings(source, destination);

  return 0;
}
