#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isPalindrome(string word) {
  int left = 0;
  int right = word.length() - 1;

  while (left < right) {
    if (word[left] != word[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
}

vector<string> PalindromeFilter(vector<string> &words, int minLength) {
  vector<string> result = {};

  for (auto word: words) {
    if (word.length() >= minLength && isPalindrome(word)) {
      result.push_back(word);
    }
  }

  return result;
}

vector<string> PalindromFilter(vector<string> words, int minLength) {
  // Just a proxy into correct spelling variant of the function
  return PalindromeFilter(words, minLength);
}

int main() {
  vector<string> tmp = {"test", "aba", "a", "aaaa", "ababa"};
  for (auto word: PalindromeFilter(tmp, 4)) {
    cout << word << endl;
  }
}
