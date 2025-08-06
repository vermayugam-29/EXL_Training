using System;
using System.Text.Json.Serialization.Metadata;
using MySql.Data.MySqlClient;

class DatabaseConnection
{
    private static string connectionString = "server=localhost;user=root;password=yugam123;database=exl";

    public static MySqlConnection Connect()
    {
        MySqlConnection connection = new MySqlConnection(connectionString);

        try
        {
            connection.Open();
            Console.WriteLine("Database connection successful!");
            return connection; 
        }
        catch (MySqlException ex)
        {
            Console.WriteLine($"Error connecting to the database: {ex.Message}");
            return null;
        }
    }
}

class DatabaseOperations
{
    public static void getAll(MySqlConnection connection)
    {
        string query = "SELECT * FROM exl.person;";

        MySqlCommand command = new MySqlCommand(query, connection);

        MySqlDataReader reader = command.ExecuteReader();

        Console.WriteLine("\nPeople in PERSON table:");
        Console.WriteLine("ID |\t Age |\t Name");
        Console.WriteLine("-------------------------");
        while (reader.Read())
        {
            Console.WriteLine($"{reader["id"]}\t{reader["age"]}\t{reader["name"]}");
        }
        reader.Close();
    }

    public static void getById(MySqlConnection connection, int id)
    {
        string query = "SELECT * FROM exl.person WHERE id = @id;";

        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@id", id);

        MySqlDataReader reader = command.ExecuteReader();
        if (reader.Read())
        {
            Console.WriteLine($"ID: {reader["id"]}, Name: {reader["name"]}, Age: {reader["age"]}");
        }
        else
        {
            Console.WriteLine("No record found with the given ID.");
        }
        reader.Close();
    }

    public static void addPerson(MySqlConnection connection)
    {
        Console.Write("Enter name: ");
        string name = Console.ReadLine();
        Console.Write("Enter age: ");
        int age = int.Parse(Console.ReadLine());

        string query = "INSERT INTO exl.person (name, age) VALUES (@name, @age);";

        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@name", name);
        command.Parameters.AddWithValue("@age", age);
        int rows = command.ExecuteNonQuery();

        Console.WriteLine(rows > 0 ? "Person added successfully." : "Failed to add person.");
    }

    public static void updatePerson(MySqlConnection connection)
    {

        Console.Write("Enter ID of the person to update: ");
        int id = int.Parse(Console.ReadLine());
        Console.Write("Enter new name: ");
        string name = Console.ReadLine();
        Console.Write("Enter new age: ");
        int age = int.Parse(Console.ReadLine());

        string query = "UPDATE exl.person SET name = @name, age = @age WHERE id = @id;";

        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@id", id);
        command.Parameters.AddWithValue("@name", name);
        command.Parameters.AddWithValue("@age", age);

        int rows = command.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Person updated successfully." : "Failed to update person please check id.");
        if (rows > 0)
        {
            Console.WriteLine($"Updated Person: ID = {id}, Name = {name}, Age = {age}");
        }
    }

    public static void deletePerson(MySqlConnection connection)
    {
        Console.Write("Enter ID of the person to delete: ");
        int id = int.Parse(Console.ReadLine());

        string query = "DELETE FROM exl.person WHERE id = @id;";

        MySqlCommand command = new MySqlCommand(query, connection);
        command.Parameters.AddWithValue("@id", id);

        int rows = command.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Person deleted successfully." : "Failed to delete person please check id.");
        if(rows > 0)
        {
            getAll(connection);
        }
    }
}