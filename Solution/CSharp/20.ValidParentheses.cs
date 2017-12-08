public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();
        foreach (var c in s) {
            if (stack.Count == 0) {
                stack.Push(c);
            } else {
                if (!IsPair(stack.Peek(), c)) {
                    stack.Push(c);
                } else {
                    stack.Pop();
                }
            }
        }
        return stack.Count == 0;
    }

    public bool IsPair(char c1, char c2) {
        if ((c1 == '(' && c2 == ')') || (c1 == ')' && c2 == '(')) {
            return true;
        } else if ((c1 == '{' && c2 == '}') || (c1 == '}' && c2 == '{')) {
            return true;
        } else if ((c1 == '[' && c2 == ']') || (c1 == ']' && c2 == '[')) {
            return true;
        }
        return false;
    }
}