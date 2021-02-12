#include <iostream>
#include <string>
#include <vector>

using namespace std;


enum Operation {
  ADD = 0,
  NEXT = 1,
  DUMP = 2,
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

int readDay() {
  int day;
  cin >> day;

  return day;
}

Operation readOperation() {
  string operation;

  cin >> operation;

  if (operation == "ADD") {
    return Operation::ADD;
  } else if (operation == "DUMP") {
    return Operation::DUMP;
  } else if (operation == "NEXT") {
    return Operation::NEXT;
  }

  return Operation::UNKNOWN;
}

void printItems(const vector<string>& items) {
  cout << items.size() << " ";
  for (auto item: items) {
    cout << item << " ";
  }

  cout << endl;
}

int main() {
  int operations = readOperations();
  int month = 0;
  vector<int> daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  vector<vector<string>> calendar(daysInMonth[month]);

  for (int tmp = 0; tmp < operations; tmp++) {
    Operation operation = readOperation();

    if (operation == Operation::ADD) {
      int day = readDay() - 1;
      string argument = readArgument();
      calendar[day].push_back(argument);
    } else if (operation == Operation::DUMP) {
      int day = readDay() - 1;
      printItems(calendar[day]);
    } else if (operation == Operation::NEXT) {
      month++;
      vector<vector<string>> newCalendar(daysInMonth[month % 12]);

      // Copy items to new month
      for (int day = 0; day < calendar.size(); day++) {
        for (auto item: calendar[day]) {
          if (day < newCalendar.size()) {
            newCalendar[day].push_back(item);
          } else {
            newCalendar[newCalendar.size() - 1].push_back(item);
          }
        }
      }

      calendar = newCalendar;
    }
  }

  return 0;
}
