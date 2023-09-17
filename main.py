from langchain.document_loaders import TextLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_company_data():
    loader = TextLoader("./company_data.txt")
    return loader.load()


# Get the data of the company you're interested in
data = get_company_data()
print(f"You have {len(data)} document(s)")

print(f"Preview of your data:\n\n{data[0].page_content[:30]}")
