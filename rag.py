import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Google Gemini API Key - supports both .env (local) and st.secrets (Streamlit Cloud)
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except Exception:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Sidebar contents
with st.sidebar:
    st.title('RAG based PDF Chat')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [Google Gemini](https://ai.google.dev/)

    ''')
    add_vertical_space(3)
    st.write('Created by PBL GROUP!')
    add_vertical_space(2)
    st.write('© 2025 PBL group')

def main():
    st.header("RAG Based PDF Reader")
    st.subheader("Your AI-Powered PDF Assistant")

    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    if pdf is not None:
        with st.spinner('Processing PDF...'):
            pdf_reader = PdfReader(pdf)

            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text=text)

            # embeddings
            store_name = pdf.name[:-4]
            st.success(f'Processing: {store_name}')

            # Initialize embeddings
            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/text-embedding-004",
                google_api_key=GOOGLE_API_KEY
            )

            # Create vector store
            try:
                # Try to load from FAISS index if it exists
                if os.path.exists(f"{store_name}.faiss"):
                    VectorStore = FAISS.load_local(
                        f"{store_name}",
                        embeddings
                    )
                    st.info('Embeddings Loaded from Disk')
                else:
                    # Create new vector store
                    VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
                    # Save the FAISS index
                    VectorStore.save_local(f"{store_name}")
                    st.success('Embeddings Computed and Saved')
            except Exception as e:
                st.error(f"An error occurred while processing embeddings: {str(e)}")
                return

            # Accept user questions/query
            query = st.text_input("Ask questions about your PDF:", placeholder="Enter your question here...")

            if query:
                try:
                    with st.spinner('Processing...'):
                        docs = VectorStore.similarity_search(query=query, k=3)
                        
                        # Initialize Gemini model
                        llm = ChatGoogleGenerativeAI(
                            model="gemini-1.5-flash",
                            google_api_key=GOOGLE_API_KEY,
                            temperature=0,
                        )
                        
                        # Create prompt template for Q&A
                        template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}

Question: {question}

Answer:"""
                        
                        prompt = PromptTemplate(
                            template=template,
                            input_variables=["context", "question"]
                        )
                        
                        # Create chain using LCEL (modern LangChain)
                        chain = prompt | llm
                        
                        # Combine docs into context
                        context = "\n\n".join([doc.page_content for doc in docs])
                        
                        # Get response
                        result = chain.invoke({"context": context, "question": query})
                        response = result.content
                        
                        # Display response
                        st.write("Answer:")
                        st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

main()
