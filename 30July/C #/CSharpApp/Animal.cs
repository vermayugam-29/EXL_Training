using System;

class Animal
{
    public String name;

    public Animal(String name)
    {
        this.name = name;
    }

    public void Speak()
    {
        Console.WriteLine($"{name} makes a sound.");
    }
}

class Dog : Animal
{
    public Dog(String name) : base(name) { }

    // public  void Speak()
    // {
    //     Console.WriteLine($"{name} Bhow Bhow.");
    // }
}