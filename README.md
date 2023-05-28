<div align="center">
  <a href="https://decathlon-chatbot.streamlit.app/">
    <img src="https://github.com/Hamagistral/decathlon-chatbot/assets/66017329/aaffa207-9f03-42b5-8c1b-a0876bc9169b" alt="Banner" width="150"><br>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Decathlon_Logo.png/1200px-Decathlon_Logo.png" alt="Banner" width="150">
  </a>

  <div id="user-content-toc">
    <ul>
      <summary><h1 style="display: inline-block;">Decathlon Chatbot and Sentiment Analysis on Reviews</h1></summary>
    </ul>
  </div>
  
  <p>A Customer Service Chatbot Trained on Decathlon Maroc Data</p>
    <a href="https://decathlon-chatbot.streamlit.app/" target="_blank">Live Preview</a>
    🏓
    <a href="https://youtu.be/GKkOpEjlfEo" target="_blank">Demo YouTube</a>
    🔮
    <a href="https://github.com/Hamagistral/DataEngineers-Glassdoor/issues" target="_blank">Request Feature</a>
</div>
<br>
<div align="center">
      <a href="https://decathlon-chatbot.streamlit.app/"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"/></a>
      <img src="https://img.shields.io/github/stars/hamagistral/decathlon-chatbot?color=blue&style=social"/>
</div>

## 📝 Table of Contents

1. [ Project Overview ](#introduction)
2. [ Sentiment Analysis & Chatbot ](#parts)
3. [ References ](#refs)
4. [ Technologies ](#techs)  
5. [ Installation ](#installation)
6.  [ Contact ](#contact)
<hr>

### 💬 Chatbot Page
![image](https://github.com/Hamagistral/decathlon-chatbot/assets/66017329/77945744-652c-4288-bc74-20f9060be7d9)


<a name="introduction"></a>
## 🔬 Project Overview :

### 🎯 Goal :

This project consists of a sentiment analysis part for product reviews and a chatbot that interacts with customers of Decathlon Maroc, a company specializing in selling sports goods. The chatbot utilizes the GPT-3.5-turbo model from OpenAI to provide information and assistance to customers.

<a name="parts"></a>
## 🤖 Sentiment Analysis & Chatbot

### 1. 😍😐😡 Sentiment Analysis :

The sentiment analysis part focuses on analyzing product reviews. It follows the following steps:

1. **Scraping:** The reviews are scraped from Decathlon Maroc's website using Beautiful Soup, extracting the necessary information for analysis like customer name, review date, review description, review rating etc... [Scraping Notebook](https://github.com/Hamagistral/decathlon-chatbot/blob/master/decathlon_scraper/scraper.ipynb)

2. **Data Cleaning:** The scraped reviews are cleaned to remove any irrelevant or noisy data like texts in arabic or numeric values, ensuring that the analysis focuses on meaningful and valid content.

3. **Sentiment Analysis:** The Natural Language Toolkit (NLTK) library and Vader sentiment analysis are employed to assess the sentiment of the review descriptions. This process provides an understanding of the customers' opinions and sentiments towards specific products. [SIA Notebook](https://github.com/Hamagistral/decathlon-chatbot/blob/master/notebook/decathlon-sentiment-analysis.ipynb)

#### 📋 Sentiment Analysis Steps :

![sia-steps](https://github.com/Hamagistral/decathlon-chatbot/assets/66017329/96b474a9-78bd-442d-9ded-34176f3bd7e6)

### 2. 💬 Chatbot :

The chatbot is designed to engage with customers and provide them with relevant information and assistance regarding various aspects of Decathlon Maroc's operations. It follows the subsequent steps:

1. **Data Extraction**: HTML files containing information about returns policies, warranty details, contact information, and other relevant topics are loaded using a WebBaseloader in Langchain.

2. **Document Embedding**: The OpenAI Ada embedding model is utilized to convert the loaded documents into embeddings, enabling efficient search and retrieval of relevant information. [Documents Embedding Notebook](https://github.com/Hamagistral/decathlon-chatbot/blob/master/notebook/embeddings.ipynb)

3. **Vector Database:** The embeddings generated from the documents are loaded into a Pinecone vector database. This database facilitates similarity searches, allowing the chatbot to retrieve the most relevant parts of the documents based on customer queries.

4. **Chatbot Interface:** A Streamlit application is developed with a chatbot interface, enabling direct interaction with customers. Customers can inquire about specific problems or request information, and the chatbot (gpt-3.5-model with custom template) leverages the Pinecone database to provide the most appropriate responses based on document similarity. [Chatbot Code](https://github.com/Hamagistral/decathlon-chatbot/blob/master/decathlon_chatbot/chatbot.py)

#### 📝 Chatbot Architecture

![chatbot-architecture](https://github.com/Hamagistral/decathlon-chatbot/assets/66017329/fbb158ad-7b8d-4a4f-a6da-94abf138bc8c)

<a name="refs"></a>
## 📋 References

**Project inspired by**: https://www.youtube.com/watch?v=cVA1RPsGQcw  
**Beautiful Scoup Scraper:** https://github.com/umangkejriwal1122/Web-Scraping  
**Streamlit Chatbot UI inspired by**: https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/

<a name="techs"></a>
## 🛠️ Technologies Used

![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<img src="https://www.jeveuxetredatascientist.fr/wp-content/uploads/2022/06/BeautifulSoup-1080x428.jpg" alt="beautifulsoup" width="75">
![Openai](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
<img src="https://www.datanami.com/wp-content/uploads/2022/03/pinecone_logo.png" alt="pinecone" width="80">
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://user-images.githubusercontent.com/66017329/223900076-e1d5c1e5-7c4d-4b73-84e7-ae7d66149bc6.png" alt="Banner" width="100">

<a name="installation"></a>
## 🖥️ Installation : 
1. Clone the repository:

```git clone https://github.com/Hamagistral/decathlon-chatbot.git```

2. Install the required packages:

```pip install -r requirements.txt```

### Usage : 

1. Change directory to `decathlon_chatbot`:

```cd decathlon_chatbot```

2. Run the app:

```streamlit run app.py```

<a name="contact"></a>
## 📨 Contact Me

[LinkedIn](https://www.linkedin.com/in/hamza-elbelghiti/) •
[Website](https://Hamagistral.me) •
[Gmail](hamza.lbelghiti@gmail.com)
