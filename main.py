import streamlit as st
import math
st.title("Quadratic Calculator")
a = int(st.text_input("Enter the 'a' variable"))
b = int(st.text_input("Enter the 'b' variable"))
c = int(st.text_input("Enter the 'c' variable"))
if st.button("Calculate"):
  st.subheader((-b+math.sqrt((b*b)-4*a*c))/2*a)
