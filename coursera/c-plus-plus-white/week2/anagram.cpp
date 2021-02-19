#include <iostream>
#include <map>
#include <string>

using namespace std;

int readTestCount() {
  int testCount;
  cin >> testCount;

  return testCount;
}

string readWord() {
  string word;
  cin >> word;

  return word;
}

map<char, int> makeCounter(string word) {
  map<char, int> counter = {};

  for (auto letter : word) {
    ++counter[letter];
  }

  return counter;
}

bool compareCounters(const map<char, int>& counterLeft, const map<char, int>& counterRight) {
  if (counterLeft.size() != counterRight.size()) {
    return false;
  }

  for (const auto& item: counterLeft) {
    if (counterRight.count(item.first) == 0 || counterRight.at(item.first) != item.second) {
      return false;
    }
  }

  return true;
}


int main() {
  int testCount = readTestCount();
  for (int test = 0; test < testCount; test++) {
    map<char, int> counterLeft = makeCounter(readWord());
    map<char, int> counterRight = makeCounter(readWord());

    if (compareCounters(counterLeft, counterRight)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
