import java.sql.*;
public class D1Sqli {
  public ResultSet getUser(Connection conn, String userId) throws SQLException {
    Statement stmt = conn.createStatement();
    String query = "SELECT * FROM users WHERE id = '" + userId + "'";
    return stmt.executeQuery(query);
  }
}
