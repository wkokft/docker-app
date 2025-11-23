from flask import Flask
import os

app = Flask(__name__)
log_path = os.getenv("LOG_PATH")

@app.route('/')
def home():
    return f"Hello from Flask backend of Wayne Kok!"

@app.route('/log')
def write_log():
    with open(f"{log_path}/waynekok_access.log", "a") as f:
        f.write("Flask route /log was accessed\n")
    return f"Updated Flask backend of Wayne!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)