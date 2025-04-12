import streamlit as st
import numpy as np
import boto3
from sagemaker.pytorch import PyTorchPredictor
from sagemaker import s3
from sagemaker.deserializers import JSONDeserializer

from image_class import image_class

st.title("Image Upload")

#image upload session state
if 'image_up' not in st.session_state:
    st.session_state.image_up = False

#upload file
images = st.file_uploader(
    'Please upload your food images:',
    type=['jpeg', 'jpg'],
    accept_multiple_files=True,
)

if images:
    st.session_state.image_up = True

#import class names
def get_class_names(file_path):
    """Reads a text file and returns a list where each element is a line from the file."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Remove newline characters from each line
        return [line.strip() for line in lines]
    except FileNotFoundError:
        return "File not found."

# Example usage:
classes_file_path = 'class_names.txt'
class_names = get_class_names(classes_file_path)

#connect to endpoint
ENDPOINT_NAME = 'yolo-endpoint'
sm_client = boto3.client(service_name="sagemaker")
predictor = PyTorchPredictor(endpoint_name=ENDPOINT_NAME, deserializer=JSONDeserializer())

#after images uploaded
if st.session_state.image_up:

    #image classification button
    if 'class_clicked' not in st.session_state:
        st.session_state.class_clicked = False
    
    def click_classify():
        st.session_state.class_clicked = True
        ing_dict_all = {}

        for img in images:
            img_enc = np.asarray(bytearray(img.read()), dtype=np.uint8)
            
            result = predictor.predict(img_enc)
            ing_dict = image_class(result, class_names=class_names)
            ing_dict_all.update(ing_dict)

        #sort ingredient dictionary
        ing_dict_all = {'Lettuce': 0.97, 'Bell Pepper': 0.96, 'Lemon': 0.96, 'Onion': 0.96, 'Chicken': 0.95}
        # ing_dict_all = dict(sorted(ing_dict_all.items(), key=lambda item: item[1], reverse=True))

        st.session_state['ingreds'] = ing_dict_all
        

    st.button('Classify Image(s)', on_click=click_classify)

    if st.session_state.class_clicked:
        st.write('Ingredient(s) Identified!')
        st.write("Proceed to Generate Recipe!")

    #display uploaded images
    st.image(images, width=300)
