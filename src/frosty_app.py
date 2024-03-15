import re
import streamlit as st
from prompts import get_system_prompt

st.title("☃️ Frosty")

# Allow HTML for custom content
st.set_option('unsafe_allow_html', True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": '模拟的content'}]

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

def remove_messages_from(index):
    st.session_state.messages = st.session_state.messages[:index]

# Display the existing chat messages
for idx, message in enumerate(st.session_state.messages):
    if message["role"] == "system":
        st.chat_message(message["role"], body=message["content"])
    else:
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.chat_message(message["role"], body=message["content"])
        with col2:
            if st.button("🗑️", key=f"remove_{idx}", help="Remove this message"):
                remove_messages_from(idx + 1)
                break

# If the last message is not from the assistant, generate a new response
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    response = '测试'
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
    st.chat_message(message["role"], body=message["content"])
