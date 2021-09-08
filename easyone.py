import streamlit as st
my_text_input = st.text_input("Type to your heart's content", "Hello World")
st.write(f"You entered: {my_text_input}")
