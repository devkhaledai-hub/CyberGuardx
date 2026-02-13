import streamlit as st

# Title
st.title("Python Basics Interactive App")
st.write("Learn Python basics interactively")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Choose Topic",
    ["Variables", "Data Types", "Numbers", "Strings", "Booleans", "Exercise"],
)


# VARIABLES
if menu == "Variables":

    st.header("Variables")

    name = st.text_input("Enter your name")
    age = st.text_input("Enter your age")
    print("name: ", name, "age: ", age)
    print(f"name: {name}, age: {age}")

    if name:
        st.write("Welcome ", name)
        st.write("Your age ", age)


# DATA TYPES
elif menu == "Data Types":

    st.header("Data Types")

    value = st.text_input("Enter something")

    if value:

        try:
            int(value)
            st.write("Type: Integer")
        except:
            try:
                float(value)
                st.write("Type: Float")
            except:
                st.write("Type: String")


# NUMBERS
elif menu == "Numbers":

    st.header("Numbers Operations")

    a = st.number_input("Enter first number", value=0)
    b = st.number_input("Enter second number", value=0)

    st.write("Addition:", a + b)
    st.write("Subtraction:", a - b)
    st.write("Multiplication:", a * b)

    if b != 0:
        st.write("Division:", a / b)


# STRINGS
elif menu == "Strings":

    st.header("Strings")

    text = st.text_input("Enter text")

    if text:

        st.write("Upper:", text.upper())
        st.write("Lower:", text.lower())
        st.write("Length:", len(text))
        st.write("Reverse:", text[::-1])


# BOOLEANS
elif menu == "Booleans":

    st.header("Booleans")

    a = st.number_input("Enter number A", value=0)
    b = st.number_input("Enter number B", value=0)

    st.write("A > B:", a > b)
    st.write("A < B:", a < b)
    st.write("A == B:", a == b)
