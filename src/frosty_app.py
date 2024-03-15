from openai import OpenAI
import re
import streamlit as st
from prompts import get_system_prompt

st.title("☃️ Frosty")

# Initialize the chat messages history
# client = OpenAI(api_key=st.secrets.OPENAI_API_KEY) 暂时移除

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": '模拟的content'}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# Function to remove messages
def remove_messages_from(index):
    st.session_state.messages = st.session_state.messages[:index]

# Display the existing chat messages
for idx, message in enumerate(st.session_state.messages):
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "results" in message:
            st.dataframe(message["results"])
        # Add a remove button for each user message
        if st.button("Remove", key=f"remove_{idx}"):
            # Remove messages from this index forward
            remove_messages_from(idx)
            # Break the loop to prevent modification during iteration
            break

# If last message is not from assistant, we need to generate a new response
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response = '测试'
        message = {"role": "assistant", "content": response}
        # Your existing code for handling responses goes here
        st.session_state.messages.append(message)
