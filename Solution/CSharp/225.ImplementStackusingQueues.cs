public class MyStack {
    Queue<int> queue;

    public MyStack() {
        queue = new Queue<int>();

        public void Push(int x) {
            queue.Enqueue(x);
        }

        public int Pop() {
            Queue<int> tempQueue = new Queue<int>();
            int count = queue.Count;
            for (int i = 0; i < count - 1; i++) {
                tempQueue.Enqueue(queue.Dequeue());
            }
            int top = queue.Dequeue();
            queue.Clear();
            count = tempQueue.Count();
            for (int i = 0; i < count; i++) {
                queue.Enqueue(tempQueue.Dequeue());
            }
            return top;
        }

        public int Top() {
            int[] arr = queue.ToArray();
            return arr[queue.Count - 1];
        }

        public bool Empty() {
            return queue.Count == 0;
        }
    }