import streamlit as st
import openai
@st.cache_resource
def connect_to_openai():
    openai.api_key = st.secrets['openai_api_key']
def generate_response(prompt):
    connect_to_openai()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating response: {e}"