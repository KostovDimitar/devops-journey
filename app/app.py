import os
from flask import Flask

app = Flask(__name__)
DATA_FILE = "/data/visits.txt"

@app.route("/")
def home():
    count = 0
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            count = int(f.read())
    count += 1
    os.makedirs("/data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        f.write(str(count))
    return f"Visits: {count}\n"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)