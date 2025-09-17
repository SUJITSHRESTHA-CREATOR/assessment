import sqlite3, json

DB_FILE = "records.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id TEXT PRIMARY KEY,
        url TEXT,
        instruction TEXT,
        parsed_fields TEXT,
        extracted TEXT,
        confidence TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def insert_record(record_id, url, instruction, fields, extracted, confidence):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO records (id, url, instruction, parsed_fields, extracted, confidence)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        record_id, url, instruction,
        json.dumps(fields), json.dumps(extracted), json.dumps(confidence)
    ))
    conn.commit()
    conn.close()
