import streamlit as st
import sqlite3
from hashlib import sha256
import subprocess
# from main import recommend_book


# Function to create a table in the database
def create_table():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
            
            
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect('user_data.db') #add file fro store the data 
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Function to check if a user exists in the database
def check_user(username, password):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Main application
def main():
    st.title("WELCOME")

    create_table()  # Create the table if it doesn't exist

    # Sidebar for registration
    st.sidebar.title("Register")
    # user_login_date = st.sidebar.date_input("date") # add date 
    new_username = st.sidebar.text_input("Username") # add  user name
    new_password = st.sidebar.text_input("Password", type='password') #add  enter user passward

    if st.sidebar.button("Register"):
        hashed_password = sha256(new_password.encode()) .hexdigest()
        add_user(new_username, hashed_password)
        st.success("Registration successful! Please log in.")

    # Main login form
    st.sidebar.title("Login")
    login_username = st.sidebar.text_input("username")  #changes st.sidebar.text_input to .user input
    login_password = st.sidebar.text_input("password", type='password')  #changes

    if st.sidebar.button("Login"):
        hashed_password = sha256(login_password.encode()).hexdigest() #convert normal number to hex code
        user = check_user(login_username, hashed_password)

        if user:
            st.success(f"Welcome, {login_username}!")
            subprocess.Popen(["streamlit","run","app.py"])   # redirect app.py 
        else:
            st.error("Invalid credentials. Please try again.")

if __name__ == "__main__":
    main()
    # recommend_book()






   