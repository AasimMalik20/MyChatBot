** LlamaIndex - Chat with my custom chatbot designed to answer questions based on my professional career**

This project builds a personalized chatbot powered by LlamaIndex, a powerful tool for indexing and retrieving information. It leverages the capabilities of GPT-3.5 and augments it with my professional data, allowing you to have informative conversations about my work experience.

Key Features:

Targeted Responses: Ask questions related to my professional background, and the chatbot will use your indexed data to provide insightful answers.
Streamlit Integration: The user interface is built with Streamlit, offering a user-friendly chat experience.
How it Works:

User Input: You can interact with the chatbot by typing your questions directly into the chat interface.
Data Retrieval: LlamaIndex seamlessly retrieves relevant information from your indexed professional data.
GPT-3.5 Augmentation: Leveraging the power of GPT-3.5, the chatbot generates comprehensive and informative responses.
Getting Started:

Prerequisites:

An OpenAI API key (instructions below)
Python 3.x
Installation:

Clone the repository:
Bash
git clone https://github.com/AasimMalik20/MyChatBot.git
Install dependencies:
pip install -r requirements.txt

Obtain an OpenAI API Key:
Visit https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key and create a new secret key.
Store the key securely in the streamlit workspace (not in the repository).

Create a Streamlit account: 
https://share.streamlit.io/
Create a new app > enter the respective details[Github link and secret key]

you can also run the app from terminal:
python streamlit run streamlit_app.py
This will launch the Streamlit app in your web browser.

Usage:

Once the app is running, simply type your questions about your professional background in the chat window and hit enter. The chatbot will analyze your query and respond using your indexed data.
