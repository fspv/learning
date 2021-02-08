#include <iostream>
#include <vector>

using namespace std;

double averageTemperature(const vector<double>& temperatures) {
  double total = 0;

  for (auto temperature: temperatures) {
    total += temperature;
  }

  return total / temperatures.size();
}

int readDays() {
  int days;
  cin >> days;
  return days;
}

void readTemperatures(vector<double>& temperatures) {
  double temperature = 0;

  for (int day = 0; day < temperatures.size(); day++) {
    cin >> temperature;
    temperatures[day] = temperature;
  }
}

int countTemperaturesAbove(const vector<double>& temperatures, double minTemperature) {
  int count = 0;
  for (auto temperature: temperatures) {
    if (temperature > minTemperature) {
      count++;
    }
  }

  return count;
}

void printTemperaturesAbove(const vector<double>& temperatures, double minTemperature) {
  int day = 0;
  for (auto temperature: temperatures) {
    if (temperature > minTemperature) {
      cout << day;
      cout << ' ';
    }
    day++;
  }
}

int main() {
  int days = readDays();
  vector<double> temperatures(days);

  readTemperatures(temperatures);

  double average = averageTemperature(temperatures);

  cout << countTemperaturesAbove(temperatures, average) << endl;

  printTemperaturesAbove(temperatures, average);

  return 0;
}
