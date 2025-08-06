using System;

class SwitchCase
{
    public static void Solve()
    {
        // Console.Write("Enter a letter : ");
        // char ch = Char.ToLower(Console.ReadKey().KeyChar);

        // switch (ch)
        // {
        //     case 'a':
        //     case 'e':
        //     case 'i':
        //     case 'o':
        //     case 'u':
        //         Console.WriteLine("\n{0} is a vowel", ch);
        //         break;
        //     default:
        //     if (Char.IsLetter(ch))
        //     {
        //         Console.WriteLine("\n{0} is a consonant", ch);
        //     }
        //     else
        //     {
        //         Console.WriteLine("\n{0} is not a letter", ch);
        //     }
        //     break;
        // }


        Console.Write("Enter a letter from VIBGYOR : ");
        char ch = Char.ToLower(Console.ReadKey().KeyChar);

        switch (ch)
        {
            case 'v':
                Console.WriteLine("\nViolet");
                break;
            case 'i':
                Console.WriteLine("\nIndigo");
                break;
            case 'b':
                Console.WriteLine("\nBlue");
                break;
            case 'g':
                Console.WriteLine("\nGreen");
                break;
            case 'y':
                Console.WriteLine("\nYellow");
                break;
            case 'o':
                Console.WriteLine("\nOrange");
                break;
            case 'r':
                Console.WriteLine("\nRed");
                break;
            default:
                Console.WriteLine("\n{0} is not a valid letter from VIBGYOR", ch);
                break;
        }
    }
}