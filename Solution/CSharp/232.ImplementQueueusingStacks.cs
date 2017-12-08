public class MyQueue {

    public Stack<int> stack;

    public MyQueue() {
        stack = new Stack<int>();
    }

    public void Push(int x) {
        stack.Push(x);
    }

    public int Pop() {
        Stack<int> tempStack = new Stack<int>();
        int count = stack.Count();
        for (int i = 0; i < count; i++) {
            tempStack.Push(stack.Pop());
        }
        int peek = tempStack.Pop();
        stack.Clear();
        count = tempStack.Count();
        for (int i = 0; i < count; i++) {
            stack.Push(tempStack.Pop());
        }
        return peek;

        public int Peek() {
            int[] arr = stack.ToArray();
            return arr[stack.Count - 1];
        }

        public bool Empty() {
            return this.stack.Count == 0;
        }
    }