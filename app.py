
import streamlit as st
from io import StringIO
from dotenv import load_dotenv
import google.generativeai as genai
import vertexai.preview.generative_models as generative_models
import os




st.set_page_config(page_title='Gemini AI Assistant', 
                    page_icon = "images/gemini_avatar.png",
                    initial_sidebar_state = 'auto')

@st.cache_data
def initialize_model():
    """
    Configure the Google generativeai with the GEMINI_API_KEY
    """
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])


initialize_model()

background_color = "#252740"

avatars = {
    "assistant" : "images/gemini_avatar.png",
    "user": "images/user_avatar.png"
}

st.markdown("<h2 style='text-align: center; color: #3184a0;'>Gemini AI Assistant</h2>", unsafe_allow_html=True)

with st.sidebar:
    st.image("images/gemini_avatar.png")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"], 
                         avatar=avatars[message["role"]]):
        st.write(message["content"])


def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"}
    ]
    
st.sidebar.button("Clear Chat History", on_click=clear_chat_history)

def run_query(input_text):
    """
    Run query. The model is initialized and then queried.
    Args:
        input_text (str): we are just passing to the model the user prompt
    Returns:
        response.text (str): the text of the response
    """
    try:

        generation_config = {
            "max_output_tokens": 8192,
            "temperature": 0.7,
            "top_p": 0.95,
        }


        model = genai.GenerativeModel("gemini-1.5-pro-001")

        conversation_context = []

        # create context
        for message in  st.session_state.messages:
            role = "User" if message["role"] == "user" else "Gemini"
            conversation_context.append(f"{role}: {message['content']}") 
        conversation_context = "\n".join(conversation_context)

        prompt = f"{conversation_context}\nYou: {input_text}\nGemini:"

        response = model.generate_content(prompt,
                                          generation_config=generation_config)

        if response:
            return response.text
        else:
            return "Error"

    except Exception as ex:
        print(ex)
        return "Error"
    

output = st.empty()
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=avatars["user"]):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        with st.spinner("Thinking..."):
            

            response = run_query(prompt)

            placeholder = st.empty()
            full_response = ""
            for item in response:
                full_response += item
                placeholder.markdown(full_response, unsafe_allow_html=True)
            placeholder.markdown(response, unsafe_allow_html=True)

    message = {"role": "assistant", 
               "content": response,
               "avatar": avatars["assistant"]}
    st.session_state.messages.append(message)