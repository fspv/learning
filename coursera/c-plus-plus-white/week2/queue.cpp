#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Operation {
  WORRY = 0,
  QUIET = 1,
  COME = 2,
  WORRY_COUNT = 3,
  UNKNOWN = -1
};

int readOperations() {
  int operations;
  cin >> operations;

  return operations;
}

Operation readOperation() {
  string operation;

  cin >> operation;

  if (operation == "WORRY") {
    return Operation::WORRY;
  } else if (operation == "QUIET") {
    return Operation::QUIET;
  } else if (operation == "COME") {
    return Operation::COME;
  } else if (operation == "WORRY_COUNT") {
    return Operation::WORRY_COUNT;
  }

  return Operation::UNKNOWN;
}

int readArgument() {
  int argument;
  cin >> argument;
  return argument;
}

int main() {
  int operations = readOperations();

  int worried = 0;
  vector<bool> people;

  for (int tmp = 0; tmp < operations; tmp++) {
    Operation operation = readOperation();
    int argument;

    if (operation == Operation::WORRY) {
      argument = readArgument();
      people[argument] = true;
      worried++;
    } else if (operation == Operation::QUIET) {
      argument = readArgument();
      people[argument] = false;
      worried--;
    } else if (operation == Operation::COME) {
      argument = readArgument();
      if (argument > 0) {
        for (int tmp1 = 0; tmp1 < argument; tmp1++) {
          people.push_back(false);
        }
      } else {
        for (int tmp1 = 0; tmp1 < -argument; tmp1++) {
          worried -= people[people.size() - 1];
          people.pop_back();
        }
      }
    } else if (operation == Operation::WORRY_COUNT) {
      cout << worried << endl;
    }
  }

  return 0;
}
