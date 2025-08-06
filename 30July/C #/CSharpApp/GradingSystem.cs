class GradingSystem
{
    public static void Solve()
    {
        Console.WriteLine("Enter your marks (0-100):");
        int marks = Convert.ToInt32(Console.ReadLine());
        string grade;

        if (marks >= 90)
        {
            grade = "A";
        }
        else if (marks >= 80)
        {
            grade = "B";
        }
        else if (marks >= 70)
        {
            grade = "C";
        }
        else if (marks >= 60)
        {
            grade = "D";
        }
        else
        {
            grade = "F";
        }

        Console.WriteLine($"Score: {marks}, Grade: {grade}");
    }
}