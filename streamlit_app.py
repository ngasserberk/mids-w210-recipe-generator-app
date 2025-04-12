import streamlit as st

#main file to run to load app
st.logo("logo.png")

#set configurations
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":taco:"
)

#page navigation
pages = [
    st.Page(
        "pages/home_page.py",
        title="Home",
        icon=":material/home:"),
    st.Page(
        "pages/image_upload.py",
        title="Upload Images",
        icon=":material/add_photo_alternate:"),
    st.Page(
        "pages/recipe_gen.py",
        title="Generate Recipe",
        icon=":material/receipt_long:"),
]

pg = st.navigation(pages)
pg.run()
