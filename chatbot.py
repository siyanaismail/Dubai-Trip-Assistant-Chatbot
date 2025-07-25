
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

initial_message = [
    {"role": "system", "content": "I am a trip planner in Dubai.I am expert in dubai Tourism, locations, hotels etc. You should respond precisely, shouldn't exceed 200 words. I am DJ here to help you."},
    {
         "role": "assistant",
         "content": "Hello, I am Dubai Genie , your expert trip planner. How can I help you?"
    }
]


def get_response_from_llm(messages):
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = initial_message

st.title("Dubai Trip Assistant App")


for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])



user_message = st.chat_input("Enter your message")
if user_message:
    new_message = {
        "role": "user",
        "content": user_message
    }
    # Append user message
    st.session_state.messages.append(new_message)
    # Get assistant response
    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message = {
            "role": "assistant",
            "content": response
        }
        st.session_state.messages.append(response_message)
    # Rerun to display both user and assistant messages immediately
    st.rerun()



