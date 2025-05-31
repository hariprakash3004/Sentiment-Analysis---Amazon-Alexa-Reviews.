import streamlit as st
import pickle
import numpy as np

# Load model and vectorizer
with open('svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Emoji dictionary
emojis = {
    0: "😠 Negative",
    1: "😐 Neutral",
    2: "😊 Positive"
}

# Color dictionary
colors = {
    0: "#FF4B4B",   # red
    1: "#FACC15",   # yellow
    2: "#4ADE80"    # green
}

# Streamlit app UI
st.set_page_config(page_title="Sentiment Predictor", page_icon="💬", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #4A90E2;'>💬 Sentiment Prediction App</h1>",
    unsafe_allow_html=True
)

st.markdown("<p style='text-align: center;'>Enter your review below and find out its sentiment!</p>", unsafe_allow_html=True)

# Input box
text_input = st.text_area("✍️ Type your review here:", height=150)

# Predict button
if st.button("Predict Sentiment 🚀"):
    if text_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Vectorize input
        text_vec = tfidf.transform([text_input])

        # Predict sentiment
        pred = model.predict(text_vec)[0]

        # Output with color and emoji
        st.markdown(
            f"<div style='background-color: {colors[pred]}; padding: 20px; border-radius: 10px; text-align: center;'>"
            f"<h2>{emojis[pred]}</h2>"
            f"</div>", unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; font-size: 12px;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
