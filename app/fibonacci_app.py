import streamlit as st

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def app():
    st.title("Fibonacci Calculator")
    n = st.number_input("Enter a number", min_value=0, step=1)
    fib = fibonacci(n)
    st.write(f"The {n}th Fibonacci number is {fib}")

if __name__ == "__main__":
    app()