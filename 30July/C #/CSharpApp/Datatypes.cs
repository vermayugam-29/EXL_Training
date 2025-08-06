using System;
using System.Runtime.InteropServices;

class Datatypes
{
    public static void Solve()
    {
        //using var - automatic type reference
        var myInt = 0;
        var myDouble = 0.0;
        var myString = "Hello, World!";
        var myBool = true;
        // int myInt = 0;
        // double myDouble = 0.0;
        // string myString = "Hello, World!";
        // bool myBool = true;

        Console.Write("Enter an integer: ");
        myInt = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter a double value : ");
        myDouble = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter a String : ");
        myString = Console.ReadLine();

        Console.Write("Enter a boolean value (true/false): ");
        myBool = Convert.ToBoolean(Console.ReadLine());

        Console.Write("Enter a character: ");
        // var myChar = Convert.ToChar(Console.ReadLine());
        var myChar = Console.ReadLine()[0];



        Console.WriteLine("You have entered the folowing data: ");
        Console.WriteLine($"Integer : {myInt}");
        Console.WriteLine($"Double : {myDouble}");
        Console.WriteLine($"String : {myString}");
        Console.WriteLine($"Boolean : {myBool}");
        Console.WriteLine($"Character : {myChar}");
    }
}