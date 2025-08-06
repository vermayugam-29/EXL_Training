using System;

class Person
{
    public String name;
    public int age;

    public Person(String name, int age)
    {
        this.name = name;
        this.age = age;
    }

    public void DisplayInfo()
    {
        Console.WriteLine($"Name : {name} , Age : {age}");
    }
}

class Student : Person
{
    public String StudentId;

    public Student(String name, int age, String StudentId) : base(name, age)
    {
        this.StudentId = StudentId;
    }

    public void DisplayStudentInfo()
    {
        DisplayInfo();
        Console.WriteLine($"StudentId :  {StudentId}.");
    }
}

class GraduateStudent : Student
{
    public String degree;

    public GraduateStudent(String name, int age, String StudentId, String degree) : base(name, age, StudentId)
    {
        this.degree = degree;
    }

    public void DisplayGraduateInfo()
    {
        DisplayStudentInfo();
        Console.WriteLine($"Degree : {degree}.");
    }
}

class Teacher : Person
{
    public String Subject;

    public Teacher(String name, int age, String Subject) : base(name, age)
    {
        this.Subject = Subject;
    }

    public void DisplayTeacherInfo()
    {
        DisplayInfo();
        Console.WriteLine($"Subject : {Subject}.");
    }
}

class Admin : Person
{
    public String Department;

    public Admin(String name, int age, String Department) : base(name, age)
    {
        this.Department = Department;
    }

    public void DisplayAdminInfo()
    {
        DisplayInfo();
        Console.WriteLine($"Department : {Department}.");
    }
}

interface ISport
{
    void PlaySport(string sportName);
}

interface IArt
{
    void PerformArt(string artType);
}

class ExtraCurricularStudent : Student, ISport, IArt
{
    public ExtraCurricularStudent(String name, int age, String StudentId) : base(name, age, StudentId) { }

    public void PlaySport(string sportName)
    {
        Console.WriteLine($"Plays : {sportName}");
    }

    public void PerformArt(string artType)
    {
        Console.WriteLine($"Performs : {artType}");
    }
    public void DisplayExtraCurricularInfo(string sportName, string artType)
    {
        DisplayStudentInfo();
        PlaySport(sportName);
        PerformArt(artType);
    }
}

class ExtraCurricularGraduateStudent : GraduateStudent, ISport, IArt
{
    public ExtraCurricularGraduateStudent(String name, int age, String StudentId, String degree) 
        : base(name, age, StudentId, degree) { }

    public void PlaySport(string sportName)
    {
        Console.WriteLine($"Plays : {sportName}");
    }

    public void PerformArt(string artType)
    {
        Console.WriteLine($"Performs : {artType}");
    }

    public void DisplayFullProfile(string sportName, string artType)
    {
        DisplayGraduateInfo();
        PlaySport(sportName);
        PerformArt(artType);
    }
}