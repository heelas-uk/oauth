import random
import streamlit as st
import string

st.title("Password generator")
characters = string.ascii_letters + string.digits + string.punctuation

num = int(st.number_input("Enter how long you want your pass to be", step=1))

password = ''.join(random.choices(characters, k=num))
st.write("Here is your password")

st.write(password)
