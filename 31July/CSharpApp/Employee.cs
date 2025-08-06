// Create a class Employee.
// Overload the PrintDetails() method in the following ways:
// No parameters → Print "No employee details provided."
// One parameter: string name → Print "Employee Name: {name}"
// Two parameters: string name, int age → Print "Employee Name: {name}, Age: {age}"
// Three parameters: string name, int age, string department → Print "Employee Name
// : {name}, Age: {age}, Department: {department}"

using System;

class Employee
{
    public void PrintDetails()
    {
        Console.WriteLine("No employee details provided.");
    }

    public void PrintDetails(string name)
    {
        Console.WriteLine($"Employee Name: {name}");
    }
    public void PrintDetails(string name, int age)
    {
        Console.WriteLine($"Employee Name: {name}, Age: {age}");
    }
    public void PrintDetails(string name, int age, string department)
    {
        Console.WriteLine($"Employee Name: {name}, Age: {age}, Department: {department}");
    }
}