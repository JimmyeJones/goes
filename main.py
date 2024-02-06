import streamlit as st
st.title("Quadratic Calculator")
a = st.text_input("Enter the 'a' variable")
if a != int():
  st.error("Your 'a' variable is not a number")
b = st.text_input("Enter the 'b' variable")
if b != int():
  st.error("Your 'b' variable is not a number")
c = st.text_input("Enter the 'c' variable")
if c != int():
  st.error("Your 'c' variable is not a number")
if st.button("Calculate"):
  st.text(a)
  st.text(b)
  st.text(c)
