from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "iot_readings.db"


st.set_page_config(
    page_title="IoT Sensor Dashboard",
    page_icon="📡",
    layout="wide",
)

st.title("IoT Sensor Dashboard")
st.write("Dashboard sederhana untuk melihat data sensor dari ESP32 Wokwi.")


def load_data(limit: int) -> pd.DataFrame:
    if not DB_PATH.exists():
        return pd.DataFrame(
            columns=["id", "device_id", "temperature", "humidity", "location", "created_at"]
        )

    connection = sqlite3.connect(DB_PATH)
    try:
        frame = pd.read_sql_query(
            """
            SELECT id, device_id, temperature, humidity, location, created_at
            FROM sensor_readings
            ORDER BY id DESC
            LIMIT ?
            """,
            connection,
            params=(limit,),
        )
    finally:
        connection.close()

    if not frame.empty:
        frame["created_at"] = pd.to_datetime(
            frame["created_at"],
            format="ISO8601",
            utc=True,
        ).dt.tz_convert("Asia/Jakarta")
        frame = frame.sort_values("created_at")

    return frame


with st.sidebar:
    st.header("Pengaturan")
    limit = st.slider("Jumlah data", min_value=10, max_value=200, value=50, step=10)
    if st.button("Refresh"):
        st.rerun()


data = load_data(limit)

if data.empty:
    st.info("Belum ada data sensor. Jalankan backend lalu kirim data dari Wokwi.")
    st.stop()

latest = data.iloc[-1]

col1, col2, col3 = st.columns(3)
col1.metric("Device", latest["device_id"])
col2.metric("Temperature", f"{latest['temperature']:.1f} °C")
col3.metric("Humidity", f"{latest['humidity']:.1f} %")

st.subheader("Grafik Sensor")
chart_data = data.set_index("created_at")[["temperature", "humidity"]]
st.line_chart(chart_data)

st.subheader("Data Terakhir")
st.dataframe(
    data.sort_values("created_at", ascending=False).reset_index(drop=True),
    use_container_width=True,
)
