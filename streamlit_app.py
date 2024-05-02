import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader

st.set_page_config(page_title="Chat with the Aasim Malik's Profile Chatbot, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets.openai_key
st.title("Chat with the Malik Aasim's Chatbot")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a professional question about Malik Aasim!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        # llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert o$
        # index = VectorStoreIndex.from_documents(docs)
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="Task: Answer questions about Aasim's professional background. Input: the user will ask questions about Aasim's professional background. Output: **Professional Summary:** Create a concise and impactful summary that showcases Aasim's value proposition and career goals. 2. **Experience:** List Aasim's work experience in reverse chronological order, detailing:* Company name, job title, and dates of employment.* Key responsibilities and accomplishments using strong action verbs.* Quantifiable results if possible e.g., increased sales by 20%). 3. **Skills:** Highlight Aasim's most relevant skills, categorizing them if necessary (e.g., technical skills, soft skills). 4. **Education & Certifications:** List Aasim's educational background, including: * Degree names, institutions, and graduation years. * Any relevant coursework or certifications. 5. **Keywords:** Include keywords relevant to Aasim's desired field for better searchability by employers."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
