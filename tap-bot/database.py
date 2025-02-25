import mysql.connector

# ✅ MySQL Connection (XAMPP default settings)
conn = mysql.connector.connect(
    host="localhost",  # XAMPP MySQL host
    user="root",       # Default user for XAMPP MySQL
    password="",       # No password by default for XAMPP MySQL
    database="tapsys_db"  # The database you created
)

cursor = conn.cursor()

def save_complaint(phone, issue, transcript):
    """Save complaint in MySQL database"""
    cursor.execute(
        "INSERT INTO complaints (phone, issue, transcript) VALUES (%s, %s, %s)",
        (phone, issue, transcript)
    )
    conn.commit()

def close_connection():
    """Close the database connection"""
    cursor.close()
    conn.close()
