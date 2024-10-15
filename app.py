# calculator_app.py

import streamlit as st

# Function definitions for calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

# Streamlit App
def main():
    st.title("🧮 Simple Calculator")

    # Initialize history in session state
    if 'history' not in st.session_state:
        st.session_state.history = []

    st.write("### Select Operation:")
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

    st.write("### Enter Numbers:")
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter first number", value=0.0, key='num1')

    with col2:
        num2 = st.number_input("Enter second number", value=0.0, key='num2')

    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
            expression = f"{num1} + {num2} = {result}"
            st.success(expression)
        elif operation == "Subtract":
            result = subtract(num1, num2)
            expression = f"{num1} - {num2} = {result}"
            st.success(expression)
        elif operation == "Multiply":
            result = multiply(num1, num2)
            expression = f"{num1} * {num2} = {result}"
            st.success(expression)
        elif operation == "Divide":
            result = divide(num1, num2)
            if isinstance(result, str):
                st.error(result)
                expression = f"{num1} / {num2} = {result}"
            else:
                expression = f"{num1} / {num2} = {result}"
                st.success(expression)
        # Add to history
        st.session_state.history.append(expression)

    st.markdown("---")
    st.write("### Calculation History")
    if st.session_state.history:
        for idx, calc in enumerate(st.session_state.history, 1):
            st.write(f"{idx}. {calc}")
    else:
        st.write("No calculations yet.")

    st.markdown("---")
    st.write("### About")
    st.write("This is a simple calculator app built with [Streamlit](https://streamlit.io/).")

if __name__ == "__main__":
    main()

