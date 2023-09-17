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
print(f"You have {len(data)} main document(s)")
## Preview of Data
# print(f"Preview of your data:\n\n{data[0].page_content[:30]}")


## Don't need at the moment
# Split up text to avoid token limits
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 800,
    chunk_overlap  = 0
)
docs = text_splitter.split_documents(data)
print (f"You now have {len(docs)} split documents")
