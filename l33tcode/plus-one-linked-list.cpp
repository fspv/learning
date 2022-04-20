struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
private:
  ListNode *reverseList(ListNode *head) {
    auto node = head;
    ListNode *prevNode = nullptr;

    while (node) {
      auto curNode = node;
      auto nextNode = node->next;

      node = nextNode;
      curNode->next = prevNode;
      prevNode = curNode;
    }

    return prevNode;
  }

public:
  ListNode *plusOne(ListNode *head) {
    auto newHead = new ListNode(0, head);
    auto reversedListHead = reverseList(newHead);

    int carry = 1;

    auto node = reversedListHead;

    while (node && carry) {
      int val = node->val;
      node->val = (val + carry) % 10;
      carry = (val + carry) / 10;
      node = node->next;
    }

    reverseList(reversedListHead);

    return newHead->val > 0 ? newHead : newHead->next;
  }
};

int main() { return 0; };
