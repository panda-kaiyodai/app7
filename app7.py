import streamlit as st

# Create a function for each arithmetic operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Create a function to perform the calculation
def calculate(operation, a, b):
    if operation == "＋":
        result = add(a, b)
    elif operation == "－":
        result = subtract(a, b)
    elif operation == "×":
        result = multiply(a, b)
    elif operation == "÷":
        result = divide(a, b)
    else:
        result = "Invalid operation"
    return result

# Create a UI for the calculator
st.title("電卓")

a = st.number_input("数字を入力してください")
b = st.number_input("数字を入力してください")

operation = st.selectbox("演算子を選んでください", ["＋", "―", "×", "÷"])

if st.button("計算する"):
    result = calculate(operation, a, b)
    st.success(result)
