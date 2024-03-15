import streamlit as st

st.title("☃️ Frosty")

# 创建两列：左侧用于聊天，右侧用于显示Markdown文本
col_chat, col_md = st.columns(2)

with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": '模拟的content'}]

    # Display the existing chat messages in the left column
    for idx, message in enumerate(st.session_state.messages):
        if message["role"] == "system":
            st.write(message["content"])
        else:
            col1, col2 = st.columns([0.9, 0.1], gap="small")
            with col1:
                st.write(message["content"])
            with col2:
                if st.button("🗑️", key=f"remove_{idx}"):
                    del st.session_state.messages[idx:]
                    break

    # Placeholder for adding space
    st.empty()

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

# 固定在底部的输入框
st.text_input("Type your message here:", key="input", on_change=lambda: st.session_state.messages.append({"role": "user", "content": st.session_state.input}), args=())
