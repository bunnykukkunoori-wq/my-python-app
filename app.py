import psycopg2
import time
from tabulate import tabulate

# Wait for PostgreSQL to be ready
time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    cursor = conn.cursor()

    # Drop old table (fixes missing columns)
    cursor.execute("DROP TABLE IF EXISTS students;")
    conn.commit()

    # Create table with new columns
    cursor.execute("""
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            course VARCHAR(50)
        );
    """)
    conn.commit()

    # Insert row
    cursor.execute("""
        INSERT INTO students (name, age, course)
        VALUES ('Bunny', 21, 'DevOps')
        RETURNING id, name, age, course;
    """)
    row = cursor.fetchone()
    conn.commit()

    # Print table format
    table = [
        ["ID", "Name", "Age", "Course"],
        [row[0], row[1], row[2], row[3]]
    ]

    print(tabulate(table, headers="firstrow", tablefmt="grid"))

    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)
