import streamlit as st
from agents.router_agent import router
from agents.ocr_agent import extract_text

st.title("KYC Verification AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded = st.file_uploader("Upload KYC document")

if uploaded:

    text = extract_text(uploaded)

    st.write("Extracted Text:")
    st.write(text)

query = st.chat_input("Ask about KYC")

if query:

    st.session_state.messages.append(
        {"role":"user","content":query}
    )

    response = router(query)

    st.chat_message("assistant").write(response)

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )