import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jaedan Parsons")
    content = """Hi, I am Jaedan! I am a C++ and Python programmer. I graduated in 2021? with a degree in Computer 
    Science and software engineering."""

    st.info(content)

# add intro to apps
st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")


# Home page






# Contact me page