# Libraries sections 
import streamlit as st
import ollama 
import time
from langchain_core.messages import AIMessage, HumanMessage

# Spécifier l'URL du serveur Ollama
#ollama_host = "http://host.docker.internal:11434"
#ollama.Client.base_url = ollama_host

# --------Functions--------------------------------------------------
def stream_data(text, delay:float=0.01):
    """Streaming function"""
    for word in text.split():
        yield word+ " "
        time.sleep(delay)

def get_response(user_question, chat_history):
    prompt = f"""
    You are a helpful assistant. Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """


    result= ollama.chat(model= "mistral", messages=[{ 'role':'user','content':prompt}])
    response = result['message']['content'] 
    return  response
# Conversation section
# Configuration de l'application Streamlit
st.set_page_config(page_title="Streamlit Chatbot", page_icon="🤖")
st.title("Chatbot")

# Chat history initialisation
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Print the chat history during the conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# Question from the user
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))  # Add the question of user to the  history

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI") and st.spinner('Thinking ...'):
        # Obtain  the  réponse from the AI
        response = get_response(user_query, st.session_state.chat_history)
        st.write_stream(stream_data(response))
      
    st.session_state.chat_history.append(AIMessage(content=response))   #Add the AI's answer to the  history


