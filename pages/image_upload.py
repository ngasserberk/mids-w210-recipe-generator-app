import streamlit as st
import image_encode as ie #python code to encode images using cv2
#import cv2
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

    #add button to classify images
    # st.button("Classify Image(s)")

    #image classification button
    if 'class_clicked' not in st.session_state:
        st.session_state.class_clicked = False
    
    def click_classify():
        #st.session_state.class_clicked = True
        st.write('Classifying Images!')
        img_list = []
        print(len(img_list))
        for i in range(len(images)):
            print(f'Image {i}')
            print(images[i])
            img_enc = ie.img_encode(images[i])
            print(img_enc)
            img_list.append(img_enc)
        print(len(img_list))

    st.button('Classify Image(s)', on_click=click_classify)

    #if st.session_state.class_clicked:
        # The message and nested widget will remain on the page
        # st.write('Classifying Images!')
        # for i in range(len(images)):
        #     print(f'Image {i}')
        #     print(images[i])



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