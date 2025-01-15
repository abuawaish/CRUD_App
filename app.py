from flask import Flask, jsonify, request , render_template
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Securely load database configuration
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'Aw@ish7')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'mydb')
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key_here')

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/execute_query', methods=['POST'])
def execute_query():
    """
    Endpoint to handle various SQL operations: custom query, insert, update, delete, and show tables.
    """
    try:
        data = request.get_json()
        operation = data.get('operation')
        query = data.get('query')  # For custom queries
        result = {}

        cursor = mysql.connection.cursor()

        if query:
            # Execute a custom SQL query
            cursor.execute(query)
            if query.strip().lower().startswith('select'):
                rows = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description or []]
                result["data"] = {f"row_{index+1}": dict(zip(column_names, row)) for index, row in enumerate(rows)}
            else:
                mysql.connection.commit()
                result["message"] = "Custom query executed successfully"

        elif operation:
            if operation == "insert":
                # Insert data into a specified table
                table_name = data.get('table_name')
                columns = data.get('columns')
                values = data.get('values')
                if not table_name or not columns or not values:
                    return jsonify({"error": "Table name, columns, and values are required for insert"}), 400
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(query)
                mysql.connection.commit()
                result["message"] = f"Data inserted successfully into table '{table_name}'"

            elif operation == "delete":
                # Delete data from a specified table
                table_name = data.get('table_name')
                condition = data.get('condition')
                if not table_name or not condition:
                    return jsonify({"error": "Table name and condition are required for delete"}), 400
                query = f"DELETE FROM {table_name} WHERE {condition}"
                cursor.execute(query)
                mysql.connection.commit()
                result["message"] = f"Data deleted successfully from table '{table_name}'"

            elif operation == "update":
                # Update data in a specified table
                table_name = data.get('table_name')
                field = data.get('field')
                condition = data.get('condition')
                if not table_name or not field or not condition:
                    return jsonify({"error": "Table name, field, and condition are required for update"}), 400
                query = f"UPDATE {table_name} SET {field} WHERE {condition}"
                cursor.execute(query)
                mysql.connection.commit()
                result["message"] = f"Data updated successfully in table '{table_name}'"

            elif operation == "show_tables":
                # Show all tables in the database
                cursor.execute("SHOW TABLES;")
                tables = cursor.fetchall()
                result["tables"] = {f"table_{index+1}": table[0] for index, table in enumerate(tables)}
            else:
                return jsonify({"error": "Invalid operation"}), 400

        else:
            return jsonify({"error": "Invalid request"}), 400

        cursor.close()

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")
