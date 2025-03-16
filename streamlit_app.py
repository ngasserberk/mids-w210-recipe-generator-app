import streamlit as st

# #title
# st.title('Recipe Generator')
st.logo("logo.png")

#set configurations
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":sushi:"
)

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
