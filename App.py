
import streamlit as st

st.set_page_config(
    page_title="F&A AI Dashboard",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ F&A SMART ENERGY & SECURITY")
st.subheader("AI SUPERVISOR DASHBOARD")
st.caption("POWERING THE FUTURE. PROTECTING WHAT MATTERS.")

st.divider()

solar = 8.0
battery = 80
demand = 12.0

col1, col2, col3 = st.columns(3)

col1.metric("Solar Production", f"{solar} kWh")
col2.metric("Battery Level", f"{battery}%")
col3.metric("Customer Demand", f"{demand} kWh")

st.divider()
st.header("🤖 AI AGENT HEALTH")

agents = {
    "Solar Agent": "ONLINE",
    "Battery Agent": "ONLINE",
    "CCTV Agent": "UNHEALTHY",
    "Customer Demand Agent": "ONLINE",
    "Predictive Agent": "ONLINE",
    "AI Supervisor": "ONLINE",
}

for agent, status in agents.items():
    if status == "ONLINE":
        st.success(f"{agent}: {status}")
    else:
        st.error(f"{agent}: {status}")

st.divider()
st.header("🚨 SYSTEM ALERTS")
st.warning("CCTV Agent needs attention. Administrator notification required.")
st.info("F&A Dashboard Version 1.0 — Simulation only.")
