#include <iostream>
#include <map>
#include <string>

using namespace std;

enum Operation {
  CHANGE_CAPITAL = 0,
  RENAME = 1,
  ABOUT = 2,
  DUMP = 3,
  UNKNOWN = -1
};

int readOperations() {
  int operations;
  cin >> operations;

  return operations;
}

string readArgument() {
  string argument;
  cin >> argument;
  return argument;
}

Operation readOperation() {
  string operation;

  cin >> operation;

  if (operation == "CHANGE_CAPITAL") {
    return Operation::CHANGE_CAPITAL;
  } else if (operation == "RENAME") {
    return Operation::RENAME;
  } else if (operation == "ABOUT") {
    return Operation::ABOUT;
  } else if (operation == "DUMP") {
    return Operation::DUMP;
  }

  return Operation::UNKNOWN;
}

int main() {
  int operations = readOperations();

  map<string, string> capitals = {};

  for (int tmp = 0; tmp < operations; tmp++) {
    Operation operation = readOperation();

    switch (operation) {
    case Operation::CHANGE_CAPITAL: {
      string country = readArgument();
      string newCapital = readArgument();
      if (capitals.count(country) > 0) {
        if (capitals[country] == newCapital) {
          cout << "Country " << country << " hasn't changed its capital"
               << endl;
        } else {
          cout << "Country " << country << " has changed its capital from "
               << capitals[country] << " to " << newCapital << endl;
          capitals[country] = newCapital;
        }
      } else {
        cout << "Introduce new country " << country << " with capital "
             << newCapital << endl;
        capitals[country] = newCapital;
      }
      break;
    }
    case Operation::RENAME: {
      string oldCountryName = readArgument();
      string newCountryName = readArgument();

      if (oldCountryName != newCountryName &&
          capitals.count(oldCountryName) > 0) {
        if (capitals.count(newCountryName) == 0) {
          string capital = capitals[oldCountryName];
          capitals.erase(oldCountryName);
          capitals[newCountryName] = capital;
          cout << "Country " << oldCountryName << " with capital " << capital
               << " has been renamed to " << newCountryName << endl;
        } else {
          cout << "Incorrect rename, skip" << endl;
        }
      } else {
        cout << "Incorrect rename, skip" << endl;
      }
      break;
    }
    case Operation::ABOUT: {
      string country = readArgument();
      if (capitals.count(country) > 0) {
        cout << "Country " << country << " has capital " << capitals[country]
             << endl;
      } else {
        cout << "Country " << country << " doesn't exist" << endl;
      }
      break;
    }
    case Operation::DUMP: {
      if (capitals.size() > 0) {
        for (auto iter : capitals) {
          string country = iter.first;
          string capital = iter.second;

          cout << country << "/" << capital << " ";
        }
        cout << endl;
      } else {
        cout << "There are no countries in the world" << endl;
      }
    }
    }
  }

  return 0;
}
