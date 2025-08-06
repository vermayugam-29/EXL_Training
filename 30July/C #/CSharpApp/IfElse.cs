class IfElse
{
    public static void Solve()
    {
        Console.Write("Enter the  number : ");
        int a = Convert.ToInt32(Console.ReadLine());

        if (a > 0)
        {
            Console.WriteLine("Positive");
        }
        else if (a < 0)
        {
            Console.WriteLine("Negative");
        }
        else
        {
            Console.WriteLine("Zero");
        }
    }
}