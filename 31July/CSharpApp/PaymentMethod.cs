using System;

public abstract class PaymentMethod
{
    public abstract void processPayment(decimal amount);
}

public class CreditCardPayment : PaymentMethod
{
    public override void processPayment(decimal amount)
    {
        Console.WriteLine($"Processing credit card payment of {amount}");
    }
}

public class PayPalPayment : PaymentMethod
{
    public override void processPayment(decimal amount)
    {
        Console.WriteLine($"Processing PayPal payment of {amount}");
    }
}

public class CryptoPayment : PaymentMethod
{
    public override void processPayment(decimal amount)
    {
        Console.WriteLine($"Processing cryptocurrency payment of {amount}");
    }
}

public class PaymemtProcessor
{
    public void Process(PaymentMethod method, decimal amount)
    {
        method.processPayment(amount);
    }
}