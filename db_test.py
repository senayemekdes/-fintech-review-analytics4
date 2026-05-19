import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="123456",
    port="5432"
)

print("Connected successfully!")

conn.close()