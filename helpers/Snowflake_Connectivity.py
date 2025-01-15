import snowflake.connector

def connect_to_snowflake():
    """
    Connect to the Snowflake database.
    Returns a connection object.
    """
    try:
        conn = snowflake.connector.connect(
            user='YOUR_USERNAME',
            password='YOUR_PASSWORD',
            account='YOUR_ACCOUNT',
            warehouse='YOUR_WAREHOUSE',
            database='YOUR_DATABASE',
            schema='YOUR_SCHEMA'
        )
        print("Connection to Snowflake successful.")
        return conn
    except Exception as e:
        print("Failed to connect to Snowflake:", e)
        return None

def fetch_data_from_snowflake(query):
    """
    Fetch data from Snowflake by executing the provided query.
    :param query: SQL query string to execute.
    :return: Query result as a list of tuples.
    """
    conn = connect_to_snowflake()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error executing query:", e)
        finally:
            conn.close()
    else:
        print("No active connection to Snowflake.")
        return None

# Example usage (replace placeholders before running):
# query = "SELECT * FROM YOUR_TABLE LIMIT 10"
# data = fetch_data_from_snowflake(query)
# print(data)
