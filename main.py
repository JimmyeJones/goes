import streamlit as st
import math
st.title("Quadratic Calculator")
a = st.text_input("Enter the 'a' variable")
b = st.text_input("Enter the 'b' variable")
c = st.text_input("Enter the 'c' variable")
if st.button("Calculate"):
  st.subheader((-b+math.sqrt((b*b)-4*a*c))/2a)
