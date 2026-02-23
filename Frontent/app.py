import streamlit as st
import sys
import os

# Add backend path
sys.path.append(os.path.abspath("../backend"))

from query import ask_question

st.set_page_config(page_title="AI SOC Knowledge Portal")

st.title("AI SOC Knowledge Assistant")
st.write("Ask anything about SOPs, KB articles, troubleshooting...")

query = st.text_input("Enter your question:")

if st.button("Search"):
    if query:
        with st.spinner("Analyzing..."):
            response = ask_question(query)
        st.success(response)
    else:
        st.warning("Please ask your question.")
