import streamlit as st

#page title
page_title = '''
<div style="text-align: center; font-size:60px">
<b>
LlamaLeftovers
</b>
</div>
'''
st.markdown(page_title, unsafe_allow_html=True)

#Company logo
left_co, cent_co,last_co = st.columns([1,1,1])
with cent_co:
    st.image("logo.png")

#Company description/mission statement
mission_statement = '''
<div style="text-align: center; font-size:30px">
Empower individuals and organizations to reduce food waste and increase access to nutritious food by developing innovative solutions that turn surplus food into delicious, creative meals.
</div>
'''
st.markdown(mission_statement, unsafe_allow_html=True)