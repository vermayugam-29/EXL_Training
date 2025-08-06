using System;
using System.Runtime.InteropServices;

class Program
{
    static void Main()
    {
        // Datatypes.Solve();
        // IfElse.Solve();
        // GradingSystem.Solve();
        // SwitchCase.Solve();
        // Operators.Solve();

        // BankAccount account = new BankAccount(1000.56);
        // account.Deposit(500.45);
        // account.Withdraw(234.78);
        // Console.WriteLine($"Current Balance: {account.GetBalance()}");
        // account.Withdraw(1266);

        // Animal animal = new Animal("Generic Animal");
        // Dog dog = new Dog("Browniiie");

        // animal.Speak();
        // dog.Speak();


        Console.WriteLine("-------------------Single Level Inheritance---------------");

        Student student = new Student("Yugam Verma", 21, "S12345");
        student.DisplayStudentInfo();

        Console.WriteLine("-------------------Multilevel  Inheritance---------------");

        GraduateStudent gradStudent = new GraduateStudent("Yugam Verma", 21, "S12345", "BE Computer Science");
        gradStudent.DisplayGraduateInfo();

        Console.WriteLine("-------------------Hierarchical  Inheritance---------------");

        Teacher teacher = new Teacher("Mr. Arun", 16, "Dotnet Programming");
        teacher.DisplayTeacherInfo();


        Admin admin = new Admin("Mr Nitish", 38, "Managing Department");
        admin.DisplayAdminInfo();

        Console.WriteLine("-------------------Multiple  Inheritance---------------");

        ExtraCurricularStudent extraCurricularStudent = new ExtraCurricularStudent("Yugam Verma", 21, "S12345");
        extraCurricularStudent.DisplayExtraCurricularInfo("Football", "Bhangra");

        Console.WriteLine("-------------------Hybrid  Inheritance---------------");
        ExtraCurricularGraduateStudent extraCurricularGraduateStudent = new ExtraCurricularGraduateStudent("Yugam Verma", 21, "S12345", "BE Computer Science");
        extraCurricularGraduateStudent.DisplayFullProfile("Football", "Bhangra");
    }
}