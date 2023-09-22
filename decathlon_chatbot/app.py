import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from chatbot import DecathlonChatbot

st.set_page_config(page_title="DecathlonChat - AI Customer Assistant", page_icon='💬')

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Decathlon_Logo.png/1200px-Decathlon_Logo.png")
    st.markdown('# 💬 DecathlonChat 🤖')
    st.markdown('''
    ---
    ### 🔮 À Propos

    Decathlon est une entreprise française de grande distribution de sport et de loisirs.

    Avec plus de 2 193 magasins répartis dans 57 pays, le groupe estime son chiffre d’affaires
    global à plus de 12,4 milliards d'euros annuellement en 2019.

    🏀🏓🏈🎳⚾🏒🥊⛳🤿🏏🎾🎿🏐⛸️

    Cette application est un chatbot qui répond aux questions des clients de Decathlon Maroc en se basant sur les informations disponibles
    sur le site web [Decathlon Maroc](https://www.decathlon.ma/).

    ###
    ''')

    st.markdown('💻 Source code on [Github](https://github.com/Hamagistral/decathlon-chatbot)')
    st.markdown('👨‍💻 Made by [Hamagistral](https://www.linkedin.com/in/hamza-elbelghiti/)')
    st.markdown('---')
    st.markdown("🔴 N.B: Ce projet est un projet personnel et n'est pas affilié à Decathlon Maroc")


if 'generated' not in st.session_state:
    st.session_state['generated'] = ["👋🏻 Bonjour! Je suis DecathlonChat, comment-puis-je vous aider ?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Salut !']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()


def get_text():
    question = st.text_input("Vous: ", "", key="input")
    return question


with input_container:
    st.markdown("### 💬 Avez-vous une question pour Decathlon Maroc ?")
    user_input = get_text()


def generate_response(prompt):
    chatbot = DecathlonChatbot()
    db = chatbot.get_db_decathlon()
    response = chatbot.get_response_from_query(db, prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i), avatar_style="bottts-neutral", seed=90)
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style="avataaars-neutral", seed=10)


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
