import requests
import sqlite3
import logging
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename="logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_PATH = "data/crypto.db"

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id TEXT PRIMARY KEY,
            name TEXT,
            symbol TEXT,
            price_usd REAL,
            price_inr REAL,
            market_cap REAL,
            last_updated TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pipeline_status (
            id INTEGER PRIMARY KEY,
            last_run TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

def fetch_and_store():
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        data = response.json()

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for coin in data:
            price_usd = coin["current_price"]
            price_inr = round(price_usd * 83, 2)

            cursor.execute("""
                INSERT OR REPLACE INTO crypto_prices
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                coin["id"],
                coin["name"],
                coin["symbol"],
                price_usd,
                price_inr,
                coin["market_cap"],
                coin["last_updated"]
            ))

        cursor.execute("DELETE FROM pipeline_status")
        cursor.execute("""
            INSERT INTO pipeline_status (last_run, status)
            VALUES (?, ?)
        """, (datetime.now().isoformat(), "SUCCESS"))

        conn.commit()
        conn.close()

        print("Pipeline ran successfully")

    except Exception as e:
        logging.error(str(e))
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pipeline_status")
        cursor.execute("""
            INSERT INTO pipeline_status (last_run, status)
            VALUES (?, ?)
        """, (datetime.now().isoformat(), "FAILED"))
        conn.commit()
        conn.close()
        print("Pipeline failed. Check logs.")

if __name__ == "__main__":
    create_tables()
    fetch_and_store()
