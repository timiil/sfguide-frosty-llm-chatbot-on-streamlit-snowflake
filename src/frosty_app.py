import streamlit as st

st.title("☃️ Frosty")

# 创建两列：左侧用于聊天和Markdown文本显示，右侧保留空白
col_chat, col_md = st.columns([0.8, 0.2])

with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": '模拟的content'}]

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

# 底部栏
st.write("---")  # 画一条分割线
col_input, col_file_uploader = st.columns([0.8, 0.2])
with col_input:
    user_input = st.text_input("Type your command here:", key="input")
with col_file_uploader:
    uploaded_file = st.file_uploader("Upload file", key="file_uploader")

# 你可以在这里添加代码来处理用户输入和文件上传
# 例如，如果用户输入了指令或上传了文件，你可以如何反馈
if user_input:
    st.write(f"You typed: {user_input}")
if uploaded_file is not None:
    st.write(f"You uploaded: {uploaded_file.name}")
