import streamlit as st


def recip_format(recipe):
    if 'title' in recipe:
        recipe_title = recipe['title']

    ing_list = []
    if 'ingredients' in recipe:
        for ing in recipe['ingredients']:
            ing_list.append(str(f"{ing['quantity']} {ing['ingredient']}"))

    instruct_list = []
    if 'instructions' in recipe:
        for instruct in recipe['instructions']:
            instruct_list.append(str(f"{instruct}"))

    if 'estimated_calories' in recipe:
        est_cal = recipe['estimated_calories']

    return recipe_title, ing_list, instruct_list, est_cal

def list_to_markdown(data, ordered=False):
    markdown_list = ""
    if ordered:
        for i, item in enumerate(data):
            markdown_list += f"{i+1}. {item}\n"
    else:
        for item in data:
            markdown_list += f"- {item}\n"
    return markdown_list