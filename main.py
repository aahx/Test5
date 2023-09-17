
"""
    Could not get UnstructuredURLLoader to work. SSL Certificate Error?
    Error Message:
        exception: Invalid file. The FileType.UNK file type is not supported in partition.
"""
from langchain.document_loaders import UnstructuredURLLoader

from langchain.document_loaders import SeleniumURLLoader # helps us load pages that require JS to render

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