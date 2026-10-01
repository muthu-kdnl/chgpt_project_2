from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = "db"
DB_NAME = "test_db"
DB_USER = "test"
DB_PASSWORD = "test_123"


@app.route("/")
def home():
    return "Hello from Application Container! Database is connected."


@app.route("/health")
def health():
    
    return "Application is healthy"


@app.route("/users")
def users():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM users;")

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify([
            {"id": row[0], "name": row[1]}
            for row in rows
        ])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)