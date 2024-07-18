import streamlit as st
import pandas  # already included with streamlit

# Home page
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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=';')

# Split number of items down middle for columns 3 & 4
num_rows = len(df)
row_split = int((num_rows / 2) + (num_rows % 2)) # the num of columns/items split in half (plus odd number if odd)

with col3:
    for index, row in df[:row_split].iterrows(): #[:10]
        st.header(row["title"])

with col4:
    for index, row in df[row_split:].iterrows(): #[10:]
        st.header(row["title"])

# Contact me page
