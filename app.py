import streamlit as st
import pandas as pd
import numpy as np

# ---------------- Page Configuration ----------------
st.set_page_config(page_title="Healio", layout="centered")

st.title("Healio – Health Monitoring Dashboard")
st.write("A prototype health monitoring application with summarized health insights.")

# ---------------- Simulated Health Data ----------------
days = 30
data = {
    "Day": list(range(1, days + 1)),
    "Steps": np.random.randint(3000, 12000, days),
    "Sleep Hours": np.round(np.random.uniform(5, 9, days), 1),
    "Calories Burned": np.random.randint(1800, 3000, days)
}

df = pd.DataFrame(data)

# ---------------- Display Raw Data ----------------
st.subheader("Daily Health Data")
st.dataframe(df)

# ---------------- ScaleDown-style Compression ----------------
st.subheader("Compressed Health Summary")

avg_steps = int(df["Steps"].mean())
avg_sleep = round(df["Sleep Hours"].mean(), 1)
avg_calories = int(df["Calories Burned"].mean())

st.metric("Average Steps", avg_steps)
st.metric("Average Sleep (hrs)", avg_sleep)
st.metric("Average Calories Burned", avg_calories)

# ---------------- Personalized Recommendations ----------------
st.subheader("Personalized Recommendations")

if avg_steps < 7000:
    st.warning("Increase physical activity to improve cardiovascular health.")
else:
    st.success("Your activity level is healthy.")

if avg_sleep < 7:
    st.warning("Try to get more sleep for better recovery.")
else:
    st.success("Your sleep duration looks good.")

st.info("This application is a demonstration prototype and not medical advice.")
