import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Community Survey Dashboard")

# Load data
df = pd.read_csv("fake_survey_data.csv")

# Sidebar filters
st.sidebar.header("Filters")
city_filter = st.sidebar.multiselect("City", df["City"].unique(), default=df["City"].unique())
age_filter = st.sidebar.multiselect("Age Group", df["Age Group"].unique(), default=df["Age Group"].unique())

filtered_df = df[(df["City"].isin(city_filter)) & (df["Age Group"].isin(age_filter))]

# Satisfaction Pie Chart
st.subheader("Satisfaction Distribution")
satisfaction_count = filtered_df["Satisfaction"].value_counts().reset_index()
satisfaction_count.columns = ["Satisfaction Level", "Count"]
fig = px.pie(satisfaction_count, values="Count", names="Satisfaction Level", title="Satisfaction Ratings")
st.plotly_chart(fig, use_container_width=True)

# Usage Bar Chart
st.subheader("Service Usage by City")
usage = filtered_df.groupby(["City", "Used Service"]).size().reset_index(name="Count")
fig2 = px.bar(usage, x="City", y="Count", color="Used Service", barmode="group", title="Service Usage")
st.plotly_chart(fig2, use_container_width=True)

# Data table
st.subheader("Filtered Survey Results")
st.dataframe(filtered_df, use_container_width=True)
