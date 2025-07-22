import streamlit as st

st.title("Chat window")

with st.chat_message("assistant"):
    st.markdown("Hello , I am AI Assistant")

with st.chat_message("human"):
    st.markdown("I am Planning Vacation to Dubai")

message = st.chat_input("Enter your Message")

if message:
    with st.chat_message("human"):
        st.markdown(message)
