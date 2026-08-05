from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, jsonify, request


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "iot_readings.db"

app = Flask(__name__)


def get_connection() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS sensor_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                location TEXT DEFAULT '',
                created_at TEXT NOT NULL
            )
            """
        )
        connection.commit()


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@app.post("/api/readings")
def create_reading():
    payload = request.get_json(silent=True) or {}

    device_id = str(payload.get("device_id", "")).strip()
    location = str(payload.get("location", "")).strip()

    try:
        temperature = float(payload["temperature"])
        humidity = float(payload["humidity"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "temperature and humidity must be numeric"}), 400

    if not device_id:
        return jsonify({"error": "device_id is required"}), 400

    created_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO sensor_readings (device_id, temperature, humidity, location, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (device_id, temperature, humidity, location, created_at),
        )
        connection.commit()
        reading_id = cursor.lastrowid

    return (
        jsonify(
            {
                "message": "reading stored",
                "id": reading_id,
                "created_at": created_at,
            }
        ),
        201,
    )


@app.get("/api/readings")
def list_readings():
    limit = request.args.get("limit", default=50, type=int)
    limit = max(1, min(limit, 500))

    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, device_id, temperature, humidity, location, created_at
            FROM sensor_readings
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return jsonify([dict(row) for row in rows]), 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
