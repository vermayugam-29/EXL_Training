using System;

class Operators
{
    public static void Solve()
    {
        int a = 10, b = 3;

        //Arithmetic Operators
        Console.WriteLine("Addition: " + (a + b));
        Console.WriteLine("Subtraction: " + (a - b));
        Console.WriteLine("Multiplication: " + (a * b));
        Console.WriteLine("Division: " + (a / b));
        Console.WriteLine("Modulus: " + (a % b) + "\n");

        //Comarison Operators
        Console.WriteLine("Equal: " + (a == b));
        Console.WriteLine("Not Equal: " + (a != b) + "\n");
        // Console.WriteLine("Greater Than: " + (a > b));
        // Console.WriteLine("Less Than: " + (a < b));

        //Logical Operators
        bool x = true, y = false;
        Console.WriteLine("Logical AND: " + (x && y));
        Console.WriteLine("Logical OR: " + (x || y));
        Console.WriteLine("Logical NOT: " + (!y));
    }
}