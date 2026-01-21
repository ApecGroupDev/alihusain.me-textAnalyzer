import streamlit as st
import re
from collections import Counter

# Page config
st.set_page_config(
    page_title="Text Analyzer",
    page_icon="📝",
    layout="centered"
)

# Hide Streamlit UI
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Text Analyzer")
st.write("Analyze your text instantly using Python.")

# Session state to store text
if "submitted" not in st.session_state:
    st.session_state.submitted = False

text = st.text_area(
    "Paste your text here",
    height=200,
    placeholder="Type or paste text here..."
)

# Analyze button
if st.button("Analyze Text"):
    st.session_state.submitted = True

# Run analysis ONLY after button click
if st.session_state.submitted and text.strip():
    # Basic counts
    characters = len(text)
    words = re.findall(r"\b\w+\b", text.lower())
    word_count = len(words)
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len([s for s in sentences if s.strip()])
    paragraphs = len([p for p in text.split("\n\n") if p.strip()])

    # Reading time (avg 200 wpm)
    reading_time = round(word_count / 200, 2)

    # Most common words
    common_words = Counter(words).most_common(10)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Characters", characters)
    col2.metric("Words", word_count)
    col3.metric("Sentences", sentence_count)
    col4.metric("Paragraphs", paragraphs)

    st.divider()

    st.subheader("Reading Time")
    st.write(f"📖 ~ {reading_time} minutes")

    st.subheader("Most Common Words")
    for word, count in common_words:
        st.write(f"**{word}** — {count}")

elif st.session_state.submitted and not text.strip():
    st.warning("Please enter some text before analyzing.")
