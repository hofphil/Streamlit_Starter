import streamlit as st
x = st.slider("Select a value",1000)
st.write(x, "squared is", x * x)