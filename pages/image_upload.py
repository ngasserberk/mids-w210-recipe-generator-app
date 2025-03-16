import streamlit as st
# from PIL import Image

st.title("Image Upload")

#image upload session state
if 'image_up' not in st.session_state:
    st.session_state.image_up = False

#upload file
images = st.file_uploader(
    'Please upload your food images:',
    type=['jpeg', 'jpg', 'png'],
    accept_multiple_files=True,
)

if images:
    st.session_state.image_up = True

#after images uploaded
if st.session_state.image_up:

    #add button to generate images
    st.button("Upload Image(s)")

    #display images
    st.image(images)


#display images
# if images is not None:



    # image = Image.open(file).convert('RGB')
    # st.image(image, use_container_width=True)

    #     #recipe generation button
    # if 'clicked' not in st.session_state:
    #     st.session_state.clicked = False

    # def click_button():
    #     st.session_state.clicked = True

    

    # st.button('Generate Recipe!', on_click=click_button)

    # if st.session_state.clicked:
    #     # The message and nested widget will remain on the page
    #     st.write('Generating Recipe!')