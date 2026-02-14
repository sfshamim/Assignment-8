import streamlit as st
import pandas as pd
import time
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

st.set_page_config(page_title="AI Based Patient Monitor", layout="wide")
st.title("🩺 AI Based Patient Monitor - ICU")

uploaded_file = st.file_uploader("Upload Patient CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.tail())

    latest = df.iloc[-1]

    st.subheader("📊 Current Vitals (Latest Minute)")
    st.write(latest)

    diagnosis_prompt = f"""
You are an ICU clinical decision support AI system.

Analyze the following patient vitals and determine:

1. Current medical condition
2. Any abnormalities
3. Urgency Level (Stable / Urgent / Emergency)
4. Recommended ICU nurse actions
5. Whether alarm activation is required

Patient Vitals:
{latest.to_dict()}
"""

    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert ICU critical care AI assistant."},
            {"role": "user", "content": diagnosis_prompt}
        ],
        temperature=0.2
    )

    latency = time.time() - start_time

    output = response.choices[0].message.content
    tokens_used = response.usage.total_tokens

    # Emergency Detection
    if "Emergency" in output:
        st.markdown(
            "<h1 style='color:red; animation: blink 1s linear infinite;'>🚨 EMERGENCY ALERT 🚨</h1>",
            unsafe_allow_html=True
        )

    st.subheader("🧠 AI Diagnosis & Suggested Actions")
    st.write(output)

    st.subheader("📡 AI Observability Metrics")
    st.write(f"⏱ Latency: {latency:.2f} seconds")
    st.write(f"🔢 Total Tokens Used: {tokens_used}")
