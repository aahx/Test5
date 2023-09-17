"""
    https://python.langchain.com/docs/use_cases/question_answering.html
"""

import os
import sys

import constants as constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]

# Load Your Documents
loader = TextLoader('./data/company_data.txt')

# Create Your Index
# Analysis and Structures the Data so you can query against it
index = VectorstoreIndexCreator().from_loaders([loader])

# Query Your Index, with Text and ChatOpenAI
print(index.query(query, llm=ChatOpenAI()))