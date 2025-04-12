import streamlit as st
import json
import requests

def call_recipe_api(ingredients, request):
    # #call recipe generation api  
    # API endpoint URL
    api_url = "enter api to your model"
    
    # Request body
    body = {
        "ingredients": ingredients,
        "request": request
    }
    
    # Convert the body to JSON
    json_body = json.dumps(body)
    # Send a POST request with JSON
    response = requests.post(
        url=api_url,
        data=json_body,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        timeout=600
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        # Print the response content
        print(response.json())
    else:
        # Print error information
        print(f"Error: {response.status_code}")
        print(response.text)

    return response.json()