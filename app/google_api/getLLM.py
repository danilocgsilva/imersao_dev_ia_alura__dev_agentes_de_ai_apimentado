from langchain_google_genai import ChatGoogleGenerativeAI
import os

def getLLM():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=os.environ.get("CHAVE_API_GOOGLE"),
        temperature=0.1
    )
    return llm
