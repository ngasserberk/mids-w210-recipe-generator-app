import streamlit as st

st.title("Generate Recipe")

col1, col2 = st.columns(
    [1, 3],
    gap="medium",
    border=True
    )

### Recipe inputs
with col1:
    st.markdown('''
    #### Ingredients detected:
    - Chicken
    - Rice
    - Chips
    ''')

    if 'redo_images' not in st.session_state:
        st.session_state.redo_images = False

    def click_redo():
        st.session_state.redo_images = True

    st.button('Reclassify Images?', on_click=click_redo)

    if st.session_state.redo_images:
        # The message and nested widget will remain on the page
        st.write('Reclassifying images')

    cuisine_input = st.text_input(
        "Desired cuisine:"
    )

    addt_notes = st.text_input(
        "Additional note for recipe:"
    )

### Recipe
with col2:
    st.markdown('''
    #### Recipe:
    ##### Ingredients:
     - 1
     - 2
     - 3
     - 4
     - 5
    ##### Instructions:
     - Step 1
     - Step 2
     - Step 3
     - Step 4
     - Step 5
    ''')