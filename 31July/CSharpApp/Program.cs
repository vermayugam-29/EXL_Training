using System;
using MySql.Data.MySqlClient;

class Program
{
    static void Main(string[] args)
    {
        //---------------------------Method Overriding Example-------------------
        // var processor = new PaymemtProcessor();
        // processor.Process(new CreditCardPayment(), 1987.40m);
        // processor.Process(new PayPalPayment(), 556.08m);
        // processor.Process(new CryptoPayment(), 2.086m);


        //------------------------Method Overloading Example--------------------------
        // Employee employee = new Employee();
        // employee.PrintDetails();
        // employee.PrintDetails("Yugam Verma");
        // employee.PrintDetails("Shivam Shukla", 21);
        // employee.PrintDetails("Sweta Shreya", 23, "IT Department");

        //------------------------Database Connection --------------------------
        MySqlConnection connection = DatabaseConnection.Connect();

        if (connection == null)
        {
            Console.WriteLine("Exiting program due to DB connection failure.");
            return;
        }


        // while (true)
        // {
        //     Console.WriteLine("Choose an option:");
        //     Console.WriteLine("1. Get all persons");
        //     Console.WriteLine("2. Get persons by ID");
        //     Console.WriteLine("3. Add person");
        //     Console.WriteLine("4. Update person");
        //     Console.WriteLine("5. Delete person");
        //     Console.WriteLine("6. Exit");


        //     Console.Write("Enter your choice: ");
        //     string choice = Console.ReadLine();

        //     switch (choice)
        //     {
        //         case "1":
        //             DatabaseOperations.getAll(connection);
        //             break;
        //         case "2":
        //             Console.Write("Enter ID: ");
        //             int id = int.Parse(Console.ReadLine());
        //             DatabaseOperations.getById(connection, id);
        //             break;
        //         case "3":
        //             DatabaseOperations.addPerson(connection);
        //             break;
        //         case "4":
        //             DatabaseOperations.updatePerson(connection);
        //             break;
        //         case "5":
        //             DatabaseOperations.deletePerson(connection);
        //             break;
        //         case "6":
        //             Console.WriteLine("Exiting the program.");
        //             connection.Close();
        //             Console.WriteLine("Database connection closed.");
        //             return;
        //         default:
        //             Console.WriteLine("Invalid choice. Please try again.");
        //             break;
        //     }
        // }


        // while (true)
        // {
        //     Console.WriteLine("\n========== Employee Onboarding System ==========");
        //     Console.WriteLine("1. View All Employees");
        //     Console.WriteLine("2. Add New Employee");
        //     Console.WriteLine("3. Update Employee");
        //     Console.WriteLine("4. Delete Employee");
        //     Console.WriteLine("5. View by Status");
        //     Console.WriteLine("6. View by Department");
        //     Console.WriteLine("7. View by Joining Date Range");
        //     Console.WriteLine("8. Exit");
        //     Console.Write("Enter your choice: ");

        //     string choice = Console.ReadLine();

        //     switch (choice)
        //     {
        //         case "1":
        //             EmployeeOnboarding.getAllEmployees(connection);
        //             break;

        //         case "2":
        //             EmployeeOnboarding.addEmployee(connection);
        //             break;

        //         case "3":
        //             EmployeeOnboarding.updateEmployee(connection);
        //             break;

        //         case "4":
        //             EmployeeOnboarding.deleteEmployee(connection);
        //             break;

        //         case "5":
        //             Console.Write("Enter status (Pending/In Progress/Completed): ");
        //             string status = Console.ReadLine();
        //             EmployeeOnboarding.getByStatus(connection, status);
        //             break;

        //         case "6":
        //             Console.Write("Enter department: ");
        //             string department = Console.ReadLine();
        //             EmployeeOnboarding.getByDepartment(connection, department);
        //             break;

        //         case "7":
        //             Console.Write("Enter start date (YYYY-MM-DD): ");
        //             string start = Console.ReadLine();
        //             Console.Write("Enter end date (YYYY-MM-DD): ");
        //             string end = Console.ReadLine();
        //             EmployeeOnboarding.getByDateRange(connection, start, end);
        //             break;

        //         case "8":
        //             Console.WriteLine("Exiting the program.");
        //             connection.Close();
        //             Console.WriteLine("Database connection closed.");
        //             return;

        //         default:
        //             Console.WriteLine("Invalid choice. Please try again.");
        //             break;
        //     }
        // }
        
        
        //-------------------------------Product Inventory System---------------------------
        while (true)
        {
            Console.WriteLine("\n========== Product Inventory System ==========");
            Console.WriteLine("1. View All Products");
            Console.WriteLine("2. Add New Product");
            Console.WriteLine("3. Update Product");
            Console.WriteLine("4. Delete Product");
            Console.WriteLine("5. Search Product by Name");
            Console.WriteLine("6. Products with stock less than 5");
            Console.WriteLine("7. Exit");
            Console.Write("Enter your choice: ");

            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    ProductInventory.getAllProducts(connection);
                    break;

                case "2":
                    ProductInventory.addProduct(connection);
                    break;

                case "3":
                    ProductInventory.updateProduct(connection);
                    break;

                case "4":
                    ProductInventory.deleteProduct(connection);
                    break;

                case "5":
                    ProductInventory.searchProduct(connection);
                    break;

                case "6":
                    ProductInventory.stockSearch(connection);
                    break;

                case "7":
                    Console.WriteLine("Exiting the program.");
                    connection.Close();
                    Console.WriteLine("Database connection closed.");
                    return;

                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}