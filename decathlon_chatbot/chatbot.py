from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import find_dotenv, load_dotenv
import streamlit as st
import pinecone

OPENAI_API_KEY = st.secrets.openai_api_key
PINECONE_API_KEY = st.secrets.pinecone_api_key
PINECONE_ENV = st.secrets.pinecone_env_key
PINECONE_INDEX = st.secrets.pinecone_index

class DecathlonChatbot:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    def get_db_decathlon(_self):
        pinecone.init(
            api_key=PINECONE_API_KEY, 
            environment=PINECONE_ENV  
        )

        index_name=PINECONE_INDEX

        db = Pinecone.from_existing_index(index_name, _self.embeddings)

        return db

    @st.cache_data(show_spinner=False)
    def get_response_from_query(_self, _db, query, k=4):
        """
        Function that generates a response to a customer question using the gpt-3.5-model and the docs provided
        """

        docs = _db.similarity_search(query, k=k)
        docs_page_content = " ".join([d.page_content for d in docs])

        chat = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

        # Template to use for the system message prompt
        template = """
            Tu es un assistant utile qui peut répondre aux questions des clients sur une plateforme de commerce électronique qui vend des équipements de sport
            nommé Decathlon basé sur ces données : {docs}. Tu agis comme un chatbot aussi, tu réponds aux phrases des utilisateurs comme "Merci", "Bonjour" etc...
           
            D'abord tu classes le sentiment de la question ou de la phrase du client, et tu utilises uniquement les informations données précédemment pour répondre à la question,
            et tu réponds en prenant compte du sentiment du client.
           
            Si tu n'as pas assez d'informations ou tu n'as pas trouvé d'informations pour répondre à la question, réponds par "Désolé, j'ignore la réponse à ta question."
            Si l'entrée n'est pas une question tu agis comme un chatbot qui aide les clients.
           
            Tes réponses doivent être courtes mais contiennent suffisamment de détails.
            """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        # Human question prompt
        human_template = "Réponds à l'entrée du client suivante : {question}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chain = LLMChain(llm=chat, prompt=chat_prompt)

        try:
            response = chain.run(question=query, docs=docs_page_content)

            return response
        except:
            return None
        
    