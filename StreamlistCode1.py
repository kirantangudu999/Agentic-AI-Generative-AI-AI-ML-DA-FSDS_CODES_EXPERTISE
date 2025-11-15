import streamlit as st
st.title("my first streamlit app created")
st.write("welcome the calculator app which calculates the square of numbers")
st.write("select a number")
st.header("pick a number")
number = st.slider("pick a number",0,100,25)
st.subheader("result")
square_number = number * number
st.write(f"the square of number {number} is {square_number} ")
