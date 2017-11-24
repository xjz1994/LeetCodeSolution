using System;

namespace ConsoleApp1
{
    class Program
    {

        public static void Sort(int[] numbers)
        {
            Sort(numbers, 0, numbers.Length - 1);
        }

        private static void Sort(int[] numbers, int left, int right)
        {
            if (left < right)
            {
                int middle = numbers[(left + right) / 2];
                int i = left - 1;
                int j = right + 1;
                while (true)
                {
                    while (numbers[++i] < middle) ;

                    while (numbers[--j] > middle) ;

                    if (i >= j)
                        break;

                    Swap(numbers, i, j);
                }

                Sort(numbers, left, i - 1);
                Sort(numbers, j + 1, right);
            }
        }

        private static void Swap(int[] numbers, int i, int j)
        {
            int number = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = number;
        }

        static void Main(string[] args)
        {
            int[] arr = {3, 4, 2, 1, 8, 7, 9, 5, 5};
            Sort(arr);
            foreach (var i in arr) {
                Console.WriteLine(i);
            }
        }
    }
}
