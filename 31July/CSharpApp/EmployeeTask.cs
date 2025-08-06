using System;
using System.Text.Json.Serialization.Metadata;
using MySql.Data.MySqlClient;

public class EmployeeOnboarding
{

    public static bool isPresent(MySqlConnection connection, string email)
    {

        string query = "SELECT COUNT(*) FROM exl.employee_onboarding WHERE email = @Email;";
        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@Email", email);

        int count = Convert.ToInt32(command.ExecuteScalar());

        if (count > 0)
        {
            connection.Close();
            return true;
        }

        return false;
    }
    public static void addEmployee(MySqlConnection connection)
    {
        Console.Write("Enter full name : ");
        string name = Console.ReadLine();

        Console.Write("Enter department : ");
        string department = Console.ReadLine();

        Console.Write("Enter email : ");
        string email = Console.ReadLine();

        if (!email.Contains("@") || !email.Contains("."))
        {
            Console.WriteLine("Invalid email format.");
            return;
        }

        if (isPresent(connection, email))
        {
            Console.WriteLine("Email already in use. Please use a different email.");
            return;
        }

        Console.Write("Enter Joining date(YYYY-MM-DD) : ");
        DateTime joiningDate = DateTime.Parse(Console.ReadLine());

        if (joiningDate < DateTime.Now)
        {
            Console.WriteLine("Joining date cannot be in the past.");
            return;
        }

        Console.Write("Enter status (Pending/ In Progress/ Completed) : ");
        string status = Console.ReadLine().ToLower().Trim();

        string[] valid = { "pending", "in progress", "completed" };
        if (!valid.Contains(status))
        {
            Console.WriteLine("Invalid status. Use one of: Pending, In Progress, Completed.");
            return;
        }

        string query =
        "INSERT INTO exl.employee_onboarding (full_name, department, email, joining_date, status) VALUES (@name, @department, @email, @joiningDate, @status);";

        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@name", name);
        command.Parameters.AddWithValue("@department", department);
        command.Parameters.AddWithValue("@email", email);
        command.Parameters.AddWithValue("@joiningDate", joiningDate);
        command.Parameters.AddWithValue("@status", status);

        int rows = command.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Employee added successfully." : "Failed to add employee.");

        if (rows > 0)
        {
            getAllEmployees(connection);
        }
    }

    public static void getAllEmployees(MySqlConnection connection)
    {
        string query = "SELECT * FROM exl.employee_onboarding;";
        MySqlCommand command = new MySqlCommand(query, connection);
        MySqlDataReader reader = command.ExecuteReader();

        Console.WriteLine("\nEmployees in the database:");
        Console.WriteLine("ID |\t Name |\t Department |\t Email |\t Joining Date |\t Status");
        Console.WriteLine("---------------------------------------------------------------");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["employee_id"]}\t{reader["full_name"]}\t{reader["department"]}\t{reader["email"]}\t{Convert.ToDateTime(reader["joining_date"]).ToString("yyyy-MM-dd")}\t{reader["status"]}");
        }
        reader.Close();

    }

    public static string[] getEmployeeById(MySqlConnection connection, int id)
    {
        string query = "SELECT * FROM exl.employee_onboarding WHERE employee_id = @id;";
        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@id", id);

        MySqlDataReader reader = command.ExecuteReader();
        string[] result = null;
        if (reader.Read())
        {
            result = new string[]
            {
                reader["full_name"].ToString(),
                reader["joining_date"].ToString(),
                reader["email"].ToString(),
                reader["department"].ToString(),
                reader["status"].ToString()
            };
        }
        reader.Close();
        return result;
    }

    public static void updateEmployee(MySqlConnection connection)
    {
        Console.Write("Enter ID of the employee to update: ");
        int id = int.Parse(Console.ReadLine());

        string[] details = getEmployeeById(connection, id);
        if (details == null)
        {
            Console.WriteLine("No employee found with the given ID.");
            return;
        }

        Console.Write("Enter new department: (optional, press Enter to skip) ");
        string department = Console.ReadLine();

        department = department == "" ? details[3] : department;

        Console.Write("Enter new email: (optional, press Enter to skip) ");
        string email = Console.ReadLine();

        if (email != "" && (!email.Contains("@") || !email.Contains(".")))
        {
            Console.WriteLine("Invalid email format.");
            return;
        }

        if (email != "" && email != details[2] && isPresent(connection, email))
        {
            Console.WriteLine("Email already in use. Please use a different email.");
            return;
        }

        email = email == "" ? details[2] : email;

        

        Console.Write("Enter status update: (optional, press Enter to skip) ");
        string status = Console.ReadLine().ToLower().Trim();
        string[] valid = { "pending", "in progress", "completed" };
        if (status != "" && !valid.Contains(status))
        {
            Console.WriteLine("Invalid status. Use one of: Pending, In Progress, Completed.");
            return;
        }

        status = status == "" ? details[4] : status;

        string query =
            "UPDATE exl.employee_onboarding SET full_name = @name, department = @department, email = @email, joining_date = @joiningDate, status = @status WHERE employee_id = @id;";

        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@id", id);
        command.Parameters.AddWithValue("@name", details[0]);
        command.Parameters.AddWithValue("@department", department);
        command.Parameters.AddWithValue("@email", email);
        command.Parameters.AddWithValue("@joiningDate", DateTime.Parse(details[1]));
        command.Parameters.AddWithValue("@status", status);

        int rows = command.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Employee updated successfully." : "Failed to update employee.");

        if (rows > 0)
        {
            getAllEmployees(connection);
        }
    }

    public static void deleteEmployee(MySqlConnection connection)
    {
        Console.Write("Enter ID of the employee to delete: ");
        int id = int.Parse(Console.ReadLine());

        string query = "DELETE FROM exl.employee_onboarding WHERE employee_id = @id;";
        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@id", id);

        Console.WriteLine("Are you sure you want to delete this employee? (Y/N)");
        string choice = Console.ReadLine().ToLower().Trim();
        if (choice == "n")
        {
            Console.WriteLine("Deletion cancelled.");
            return;
        }
        else if (choice != "y" && choice != "n")
        {
            Console.WriteLine("Invalid input. Deletion cancelled.");
            return;
        }

        int rows = command.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Employee deleted successfully." : "Failed to delete employee please check id.");

        if (rows > 0)
        {
            getAllEmployees(connection);
        }
    }

    public static void getByStatus(MySqlConnection connection, string status)
    {
        string query = "SELECT * FROM exl.employee_onboarding WHERE status = @status;";
        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@status", status);

        MySqlDataReader reader = command.ExecuteReader();
        Console.WriteLine($"\nEmployees with status '{status}':");
        Console.WriteLine("ID |\t Name \t Department |\t Email |\t Joining Date |\t Status");
        Console.WriteLine("---------------------------------------------------------------");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["employee_id"]}\t{reader["full_name"]}\t{reader["department"]}\t{reader["email"]}\t{Convert.ToDateTime(reader["joining_date"]).ToString("yyyy-MM-dd")}\t{reader["status"]}");
        }
        reader.Close();
    }

    public static void getByDepartment(MySqlConnection connection, string department)
    {
        string query = "SELECT * FROM exl.employee_onboarding WHERE department = @department;";
        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@department", department);

        MySqlDataReader reader = command.ExecuteReader();
        Console.WriteLine($"\nEmployees in department '{department}':");
        Console.WriteLine("ID |\t Name |\t Department |\t Email |\t Joining Date |\t Status");
        Console.WriteLine("---------------------------------------------------------------");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["employee_id"]}\t{reader["full_name"]}\t{reader["department"]}\t{reader["email"]}\t{Convert.ToDateTime(reader["joining_date"]).ToString("yyyy-MM-dd")}\t{reader["status"]}");
        }
        reader.Close();
    }

    public static void getByDateRange(MySqlConnection connection, string start, string end)
    {
        string query = "SELECT * FROM exl.employee_onboarding WHERE joining_date BETWEEN @start AND @end;";
        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@start", DateTime.Parse(start));
        command.Parameters.AddWithValue("@end", DateTime.Parse(end));

        MySqlDataReader reader = command.ExecuteReader();
        Console.WriteLine($"\nEmployees who joined between {start} and {end}:");
        Console.WriteLine("ID |\t Name |\t Department |\t Email |\t Joining Date |\t Status");
        Console.WriteLine("---------------------------------------------------------------");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["employee_id"]}\t{reader["full_name"]}\t{reader["department"]}\t{reader["email"]}\t{Convert.ToDateTime(reader["joining_date"]).ToString("yyyy-MM-dd")}\t{reader["status"]}");
        }
        reader.Close();
    }
}
