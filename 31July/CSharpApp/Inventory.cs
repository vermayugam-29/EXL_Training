using System;
using MySql.Data.MySqlClient;
class ProductInventory
{
    public static void addProduct(MySqlConnection conn)
    {
        Console.Write("Enter product name: ");
        string name = Console.ReadLine();

        Console.Write("Enter category: ");
        string category = Console.ReadLine();

        Console.Write("Enter price: ");
        decimal price = decimal.Parse(Console.ReadLine());

        Console.Write("Enter stock available: ");
        int stock = int.Parse(Console.ReadLine());

        if (name == "" || category == "" || price <= 0 || stock < 0)
        {
            Console.WriteLine("All the fields are required and numeric data should be positive.");
            return;
        }

        string query = "INSERT INTO exl.products (product_name,category,price,stock_qty) VALUES (@name, @category, @price, @stock)";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@name", name);
        cmd.Parameters.AddWithValue("@category", category);
        cmd.Parameters.AddWithValue("@price", price);
        cmd.Parameters.AddWithValue("@stock", stock);

        int rows = cmd.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Product added successfully." : "Failed to add product.");
    }

    public static void getAllProducts(MySqlConnection conn)
    {
        string query = "SELECT * FROM exl.products";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        MySqlDataReader reader = cmd.ExecuteReader();

        printTableHeader();

        while (reader.Read())
        {
            printProductRow(reader);
        }

        reader.Close();
    }

    public static string[] getProductById(MySqlConnection conn, int id)
    {
        string query = "SELECT * FROM exl.products WHERE product_id = @id";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@id", id);

        MySqlDataReader reader = cmd.ExecuteReader();

        if (reader.Read())
        {
            string[] productDetails = new string[5];
            productDetails[0] = reader["product_id"].ToString();
            productDetails[1] = reader["product_name"].ToString();
            productDetails[2] = reader["category"].ToString();
            productDetails[3] = reader["price"].ToString();
            productDetails[4] = reader["stock_qty"].ToString();
            reader.Close();
            return productDetails;
        }
        else
        {
            reader.Close();
            return null;
        }
    }

    public static void updateProduct(MySqlConnection conn)
    {
        Console.Write("Enter product ID to update: ");
        int id = int.Parse(Console.ReadLine());

        string[] productDetails = getProductById(conn, id);
        if (productDetails == null)
        {
            Console.WriteLine("Product not found.");
            return;
        }


        Console.Write("Enter updated price of product (optional, press Enter to skip): ");
        string price_input = Console.ReadLine();
        decimal price;

        if (string.IsNullOrWhiteSpace(price_input))
        {
            price = decimal.Parse(productDetails[3]);
        }
        else
        {
            price = decimal.Parse(price_input); 
            if (price <= 0)
            {
                Console.WriteLine("Invalid price. Keeping old price.");
                price = decimal.Parse(productDetails[3]);
            }
        }

        Console.Write("Enter updated stock available (optional, press Enter to skip): ");
        string stock_input = Console.ReadLine();
        int stock;

        if (string.IsNullOrWhiteSpace(stock_input))
        {
            stock = int.Parse(productDetails[4]);
        }
        else
        {
            stock = int.Parse(stock_input);
            if (stock < 0)
            {
                Console.WriteLine("Invalid stock. Keeping old stock.");
                stock = int.Parse(productDetails[4]);
            }
        }



        string query = "UPDATE exl.products SET price = @price, stock_qty = @stock WHERE product_id = @id";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@price", price);
        cmd.Parameters.AddWithValue("@stock", stock);
        cmd.Parameters.AddWithValue("@id", id);

        int rows = cmd.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Product updated successfully." : "Failed to update product.");
    }

    public static void deleteProduct(MySqlConnection conn)
    {
        Console.Write("Enter product ID to delete: ");
        int id = int.Parse(Console.ReadLine());

        string query = "DELETE FROM exl.products WHERE product_id = @id";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@id", id);

        int rows = cmd.ExecuteNonQuery();
        Console.WriteLine(rows > 0 ? "Product deleted successfully." : "Failed to delete product.");
    }

    public static void searchProduct(MySqlConnection conn)
    {
        Console.Write("Enter product name to search: ");
        string name = Console.ReadLine();

        string query = "SELECT * FROM exl.products WHERE product_name LIKE @name";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@name", "%" + name + "%");

        MySqlDataReader reader = cmd.ExecuteReader();

        if (!reader.HasRows)
        {
            Console.WriteLine("No products found.");
        }
        else
        {
            printTableHeader();
            while (reader.Read())
            {
                printProductRow(reader);
            }
        }

        reader.Close();
    }

    public static void stockSearch(MySqlConnection conn)
    {
        string query = "SELECT * FROM exl.products WHERE stock_qty < 5";
        MySqlCommand cmd = new MySqlCommand(query, conn);
        MySqlDataReader reader = cmd.ExecuteReader();

        if (!reader.HasRows)
        {
            Console.WriteLine("All products have sufficient stock.");
        }
        else
        {
            Console.WriteLine("Products with low stock:");
            printTableHeader();
            while (reader.Read())
            {
                printProductRow(reader);
            }
        }

        reader.Close();
    }

    public static void printTableHeader()
    {
        Console.WriteLine(new string('-', 78));
        Console.WriteLine($"| {"ID",-5} | {"Name",-20} | {"Category",-15} | {"Price",-10} | {"Stock",-8} |");
        Console.WriteLine(new string('-', 78));
    }

    public static void printProductRow(MySqlDataReader reader)
    {
        Console.WriteLine($"| {reader["product_id"],-5} | {reader["product_name"],-20} | {reader["category"],-15} | {reader["price"],-10} | {reader["stock_qty"],-8} |");
    }
}
