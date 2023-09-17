# Helps load pages that require JS to render
from langchain.document_loaders import SeleniumURLLoader 


from langchain.chains.summarize import load_summarize_chain  # Summarize Chain
from langchain.llms import OpenAI  # Our Language Model
from langchain.prompts import PromptTemplate  # Prompt Templates
from langchain.text_splitter import RecursiveCharacterTextSplitter # Split up our Documents


def get_company_page():   
    urls = [
        "https://www.tesla.com/about"
    ]
    loader = SeleniumURLLoader(urls=urls)
    return loader.load()

# Get the data of the company you're interested in
data = get_company_page()
print (f"You have {len(data)} document(s)")