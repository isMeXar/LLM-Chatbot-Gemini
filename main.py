import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = []

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Display the chat history
for message in st.session_state.chat_session:
    with st.chat_message(translate_role_for_streamlit(message['role'])):
        st.markdown(message['text'])

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Add user's message to chat and display it
    st.session_state.chat_session.append({'role': 'user', 'text': user_prompt})

    # Send user's message to Gemini-Pro and get the response
    headers = {"Authorization": f"Bearer {GOOGLE_API_KEY}"}
    data = {"prompt": user_prompt}
    response = requests.post("https://api.generativeai.dev/v1/chat/gemini-pro-latest", headers=headers, json=data)
    gemini_response = response.json()

    # Display Gemini-Pro's response
    st.session_state.chat_session.append({'role': 'assistant', 'text': gemini_response['text']})
