# ==========================================
# Task 02: Exploratory Data Analysis (EDA)
# Streamlit Application
# ==========================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# Page Configuration
# ------------------------------------------
st.set_page_config(
    page_title="Task 02 - EDA Dashboard",
    layout="wide"
)

st.title("📊 Task 02: Exploratory Data Analysis (EDA)")
st.write("Student Performance Dataset Analysis")

# ------------------------------------------
# Load Dataset
# ------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("task02_student_performance.csv")

df = load_data()

# ------------------------------------------
# Display Raw Data
# ------------------------------------------
st.subheader("📁 Dataset Preview")
st.dataframe(df)

# ------------------------------------------
# Dataset Summary
# ------------------------------------------
st.subheader("📌 Dataset Summary")

col1, col2 = st.columns(2)

with col1:
    st.write("**Dataset Shape (Rows, Columns):**")
    st.write(df.shape)

with col2:
    st.write("**Missing Values Per Column:**")
    st.write(df.isnull().sum())

# ------------------------------------------
# Statistical Summary
# ------------------------------------------
st.subheader("📈 Statistical Summary")
st.dataframe(df.describe())

# ------------------------------------------
# Sidebar Filters
# ------------------------------------------
st.sidebar.header("🔍 Filters (Task 02)")

gender_filter = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[df["Gender"].isin(gender_filter)]

# ------------------------------------------
# Visualizations
# ------------------------------------------
st.subheader("📊 Visualizations")

# ---------- Histogram ----------
st.markdown("### 📌 Distribution of Math Scores")

fig1, ax1 = plt.subplots()
ax1.hist(filtered_df["MathScore"], bins=10)
ax1.set_xlabel("Math Score")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# ---------- Bar Chart ----------
st.markdown("### 📌 Average Subject Scores by Gender")

avg_scores = (
    filtered_df
    .groupby("Gender")[["MathScore", "ScienceScore", "EnglishScore"]]
    .mean()
)

fig2, ax2 = plt.subplots()
avg_scores.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Gender")
ax2.set_ylabel("Average Score")
st.pyplot(fig2)


