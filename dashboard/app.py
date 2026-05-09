import streamlit as st
import json
import time

st.title("🚗 Real-Time HIL Dashboard")

placeholder = st.empty()

while True:

    try:

        with open("logs/live_log.json", "r") as f:
            logs = json.load(f)

        latest_logs = logs[-10:]

        with placeholder.container():

            for item in reversed(latest_logs):

                st.subheader("⏱ " + item["timestamp"])

                st.write("### 📡 Sensor Data")
                st.json(item["sensor_data"])

                st.write("### 🧠 ECU Result")
                st.write(item["ecu_result"])

                if item["status"] == "PASS":
                    st.success(item["status"])
                else:
                    st.error(item["status"])

                st.divider()

    except:
        st.write("Waiting for live data...")

    time.sleep(1)