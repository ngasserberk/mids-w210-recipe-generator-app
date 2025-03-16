import streamlit as st

#page title
st.title("Welcome to [COMPANY NAME]!")

#Company logo
st.image("logo.png")

#Company description/mission statement
mission_statement = '''
<center>
Empower individuals and organizations to reduce food waste and increase access to nutritious food by developing innovative solutions that turn surplus food into delicious, creative meals.
</center>
'''
st.markdown(mission_statement)