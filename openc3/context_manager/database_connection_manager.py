"""
Create a context manager for database connections that handles errors at different levels
"""

class DatabaseConnection:
    """
    Context manager that:
    - Connects to a database
    - Handles connection errors gracefully
    - Rolls back on query errors
    - Always closes connection
    - Logs all errors
    """
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.transaction_active = False

    def __enter__(self):
        """
        Connect to database.
        If connection fails, raise ConnectionError.
        """
        pass  # Your code here

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If exception occurred during queries:
        - Rollback if transaction active
        - Log the error
        - Don't suppress the exception

        Always:
        - Close connection
        """
        pass  # Your code here

    def execute(self, query):
        """
        Execute a query.
        Start transaction if not active.
        """
        pass  # Your code here

# Mock database for testing:
class MockDB:
    def __init__(self, fail_on_connect=False):
        self.fail_on_connect = fail_on_connect
        self.closed = False
        self.transaction_active = False

    def connect(self, connection_string):
        if self.fail_on_connect:
            raise ConnectionError("Failed to connect")
        return self

    def execute(self, query):
        if "FAIL" in query:
            raise ValueError("Query error")
        return "Success"

    def rollback(self):
        self.transaction_active = False
        print("Transaction rolled back")

    def close(self):
        self.closed = True
        print("Connection closed")

# Test it:
try:
    with DatabaseConnection("localhost:5432") as db:
        db.execute("SELECT * FROM users")
        db.execute("UPDATE users SET name = 'FAIL'")  # This should rollback
except ValueError:
    print("Query failed, but connection was cleaned up")