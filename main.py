import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

opr = st.selectbox(
    "Choose operator",
    ["+", "-", "*", "%"]
)

def calculate(num1, opr, num2):

    if opr == "+":
        return num1 + num2

    elif opr == "-":
        return num1 - num2

    elif opr == "*":
        return num1 * num2

    elif opr == "%":
        return num1 % num2

result = calculate(num1, opr, num2)

st.write("Result =", result)