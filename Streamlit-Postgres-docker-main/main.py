import streamlit as st
import psycopg2

# Database connection
conn = psycopg2.connect(
    host="my_postgres_container",
    database="testdb",
    user="rahul",
    password="secret"
)
cur = conn.cursor()

# Fetch data from table
cur.execute("SELECT * FROM passengers;")
data = cur.fetchall()

# Streamlit UI
st.title("🚄 Passenger Data")
for row in data:
    st.write(f"ID: {row[0]}, Name: {row[1]}, Location: {row[2]}")

cur.close()
conn.close()
