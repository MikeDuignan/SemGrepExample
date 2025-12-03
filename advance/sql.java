import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class VulnerableSQLExample {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter username: ");
        String userInput = scanner.nextLine();

        try {
            Connection conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/testdb", "root", "password");

            Statement stmt = conn.createStatement();

            // ❌ VULNERABLE: user input is concatenated directly into SQL query
            String query = "SELECT * FROM users WHERE username = '" + userInput + "';";

            System.out.println("Running query: " + query);

            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("User found: " + rs.getString("username"));
            }

            conn.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
