import random
import streamlit as st
import string

import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Microsoft", on_click=st.login)

if not st.experimental_user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.experimental_user.name}!")
    st.button("Log out", on_click=st.logout)
  
    st.title("Password generator")
    characters = string.ascii_letters + string.digits + string.punctuation
  
    num = int(st.number_input("Enter how long you want your pass to be", step=1))
  
    password = ''.join(random.choices(characters, k=num))
    st.write("Here is your password")
    
    st.write(password)
