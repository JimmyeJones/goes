import streamlit as st
st.title("Quadratic Calculator")
a = st.text_input("Enter the 'a' variable")
b = st.text_input("Enter the 'b' variable")
c = st.text_input("Enter the 'c' variable")
if st.button("Calculate"):
  st.text(a)
  st.text(b)
  st.text(c)
