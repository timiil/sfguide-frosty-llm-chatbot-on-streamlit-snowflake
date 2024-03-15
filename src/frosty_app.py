import streamlit as st
import datetime

st.title("☃️ 文字实验室")

# 创建两列：左侧用于聊天，右侧用于显示Markdown文本
col_chat, col_md = st.columns(2)

with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": '模拟的content'}]

    # Display the existing chat messages in the left column
    for idx, message in enumerate(st.session_state.messages):
        if message["role"] == "system":
            st.write(f"**System**: {message['content']}")
        else:
            col1, col2 = st.columns([0.9, 0.1], gap="small")
            with col1:
                st.write(f"**User**: {message['content']}")
            with col2:
                if st.button("🗑️", key=f"remove_{idx}"):
                    del st.session_state.messages[idx:]
                    break

    # Input and send button
    input_col, send_col = st.columns([9, 1])
    with input_col:
        user_input = st.text_input("Type your message here:", key="input", on_change=None)
    with send_col:
        send_button = st.button("Send")

    if send_button:
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.input = ""  # 清空输入框

            # 模拟系统回复
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.messages.append({"role": "system", "content": f"当前时间是: {current_time}"})

with col_md:
    # 在右侧列中渲染Markdown文本
    md_content = """
    ## 测试Markdown内容

    这是一段**粗体文本**。

    - 这是一个列表项
    - 另一个列表项
    - 子列表项

    > 这是一个引用。

    `代码块显示`

    ```
    多行代码块
    line 2
    line 3
    ```
    """
    st.markdown(md_content)
