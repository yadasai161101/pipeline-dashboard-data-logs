import sqlite3
import json

conn = sqlite3.connect("data/crypto.db")
cursor = conn.cursor()

cursor.execute("SELECT name, price_usd, price_inr FROM crypto_prices")
cryptos = [
    {"name": r[0], "price_usd": r[1], "price_inr": r[2]}
    for r in cursor.fetchall()
]

cursor.execute("SELECT last_run, status FROM pipeline_status")
status = cursor.fetchone()

output = {
    "status": status[1],
    "last_run": status[0],
    "cryptos": cryptos
}

with open("dashboard/data.json", "w") as f:
    json.dump(output, f, indent=2)

conn.close()
