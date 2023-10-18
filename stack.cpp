#include <unordered_map>
#include <stack>
#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {

        unordered_map<char, char> Mmap = {
            {')', '('},
            {'}', '{'},
            {']', '['}};
        stack<char> myStack;

        for (const auto &c : s)
        {
            if (Mmap.find(c) != Mmap.end())
            {
                if (myStack.empty())
                {
                    return false;
                }
                if (myStack.top() != Mmap[c])
                {
                    return false;
                }
                myStack.pop();
            }
            else
            {
                myStack.push(c);
            }
        }

        return myStack.empty();
    }
};

int main()
{
    Solution s;
    cout << s.isValid("()[]{}") << endl;
}