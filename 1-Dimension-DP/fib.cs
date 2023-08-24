using System;

class fib
{
    static int ClimbStairs(int n)
    {
        if (n <= 2)
        {
            return 1;
        }

        int one = 1, two = 1;

        for (int i = 0; i < n; i++)
        {
            int temp = one;
            one = one + two;
            two = temp;
        }

        return one;
    }

    static void Main(string[] args)
    {
        Console.WriteLine(ClimbStairs(5));
    }
}