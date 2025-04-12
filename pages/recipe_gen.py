import streamlit as st
import json
import requests

from recipe_gen_api import call_recipe_api
from recipe_format import recip_format, list_to_markdown

st.title("Generate Recipe")

col1, col2 = st.columns(
    [1, 3],
    gap="medium",
    border=True
    )

ing_to_select=[]
if 'ingreds' in st.session_state:
    ingred_dict = st.session_state['ingreds']
    #create list to display in selection pop-up
    ing_to_select = [f"{key}: {value:.0%}" for key, value in ingred_dict.items()]

selcted_ings_l2 = []
manual_ings_l2 = []
manual_ings_d = {}

gen_recip=''
recipe_title = ''
ing_list = []
instruct_list = []
est_cal = ''
### Recipe inputs
with col1:
    #select ingredients from classification model
    selected_ings_l = st.multiselect("Verify/select identified your ingredients:", options=ing_to_select)
    selcted_ings_l2 = [ing.split(':')[0].strip() for ing in selected_ings_l]
    selected_ings_d = {i:ingred_dict[i] for i in selcted_ings_l2}

    #manually add additional ingredients
    manual_ings_l= st.text_input("Type additional ingredients you'd like in your recipe. Please separate using a comma.")
    if len(manual_ings_l)>0:
        st.write('Additional ingredients added!')
        manual_ings_l2 = [ing.strip() for ing in manual_ings_l.split(',')]
        manual_ings_d = {i:100 for i in manual_ings_l2}
    
    #Cuisine type
    cuis_to_select = ['American', 'Italian', 'Chinese', 'Mexican', 'Indian']
    cuis_to_select = sorted(cuis_to_select)
    cuisine_input = st.multiselect("Desired cuisine:", options=cuis_to_select)

    #additional notes
    addt_notes = st.text_input("Additional note for recipe:")
    if len(addt_notes)>0:
        st.write('Additional information added!')

    #Generate recipe
    if 'gen_recip' not in st.session_state:
        st.session_state.gen_recip = False

    def click_gen_recip():
        st.session_state.gen_recip = True

    st.button('Generate Recipe!', on_click=click_gen_recip)

    if st.session_state.gen_recip:
        # The message and nested widget will remain on the page
        st.write('Generating Recipe!')

        #if just using ingredient list
        ings_to_llm = []
        ings_to_llm += manual_ings_l2
        ings_to_llm += selcted_ings_l2
        
        #build user pref string to send to prompt
        if len(addt_notes)>0 and len(cuisine_input)>0:
            cuis_str = ", ".join(cuisine_input)
            user_pref = addt_notes + " with cuisine type " + cuis_str
        elif len(addt_notes)>0:
            user_pref = addt_notes
        elif len(cuisine_input)>0:
            cuis_str = ", ".join(cuis_to_select)
            user_pref = "with cuisine type " + cuis_str
        else:
            user_pref = ''
        
        gen_recip = call_recipe_api(ingredients=ings_to_llm, request=user_pref)
        print(gen_recip)

        recipe_title, ing_list, instruct_list, est_cal = recip_format(gen_recip)


### Recipe
with col2:
    # st.write(gen_recip)
    
    # Recipe title:
    st.title(recipe_title)

    # Estimated calories:
    if est_cal:
        st.markdown(f"**Estimated calories**: {est_cal}")
    
    # Ingredients:
    if ing_list:
        st.markdown("**Ingredients**:")
        markdown_ings = list_to_markdown(ing_list)
        st.markdown(markdown_ings)
    
    # Instructions:
    if instruct_list:
        st.markdown("**Instructions**:")
        markdown_instruct = list_to_markdown(instruct_list, ordered=True)
        st.markdown(markdown_instruct)