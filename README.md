# GeminiPro Chatbot 🤖

GeminiPro Chatbot is an interactive AI-powered assistant built with **Streamlit** and **Google Gemini-Pro**. This project demonstrates how to deploy Large Language Models (LLMs) in a user-friendly interface and customize chatbot behavior for various audiences or use cases.


## Technologies Used
- **Python**: Backend programming language.
- **Google Gemini-Pro**: Generative AI for conversational responses.
- **Streamlit**: For building the user interface.


## Features
- **LLM Integration**: Uses Google Gemini-Pro for conversational responses.
- **Customizable Behavior**: Chatbot behavior can be tailored for specific audiences (e.g., adults, children, or professional use cases).
- **Interactive Interface**: Built with Streamlit for a clean, easy-to-use design



## Installation and Setup

Follow these steps to get the chatbot running on your local machine:

### Step 1: Clone the Repository
Clone the project from GitHub to your local machine:
```bash
git clone https://github.com/isMeXar/gemini-pro-chatbot.git
cd gemini-pro-chatbot-main
```

### Step 2: Install Dependencies
Install the necessary Python packages using pip. Make sure you have Python 3.10+ installed:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a .env file in the root directory of the project and add your Google API key. This API key is required to access the Gemini-Pro model:
```bash
GOOGLE_API_KEY=your_google_api_key
```
### Step 4: Run the Application
Launch the Streamlit application using the command below:
```bash
streamlit run app.py
```

### Step 5: Access the Chatbot
Once the server starts, it will provide a URL (e.g., http://localhost:8501). Open this URL in your web browser to start interacting with the chatbot.


## Future Improvements

- **History Feature**: Save and revisit past interactions for a more personalized experience.
- **Enhanced Design**: Improve the UI with a more polished look and additional features.
- **Additional Functionalities**:
  - Support multiple languages for broader accessibility.
  - Allow advanced customization of chatbot tone and personality.
  - Implement content moderation for diverse audiences.


## Conclusion
This project provides an interactive and customizable AI experience using Google Gemini-Pro and Streamlit. With potential for future enhancements, this project offers a foundation for building advanced conversational agents tailored to different use cases and audiences.

