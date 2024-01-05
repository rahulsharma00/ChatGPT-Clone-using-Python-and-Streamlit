import streamlit as st
from streamlit_chat import  message
from dotenv import load_dotenv
import os 

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage, # Role, First message in the conversation
    HumanMessage,
    AIMessage # Response from the langauge model
)

def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title='Gpt Clone', page_icon="🤖")


def main():

    init()
    chat = ChatOpenAI(temperature=0) # How random you want the response to be

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant")
                    ]


    st.header('Your own ChatGPT', divider='rainbow')

    

    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

        if user_input:
            # message(user_input, is_user=True)
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Beep Boop I'm thinking..."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            # message(response.content, is_user=False)
    
    messages = st.session_state.get('messages', [])
    for i, msg, in enumerate(messages[1:]):
        if i%2==0:
            message(msg.content, is_user=True, key=str(i)+ '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')

if __name__ == '__main__':
    main()