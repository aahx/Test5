# https://www.youtube.com/watch?v=y1pyAQM-3Bo
# Sales Email with Greg Kamradt

import os
import constants as constants

from langchain.document_loaders import TextLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["OPENAI_API_KEY"] = constants.APIKEY

prospect_info_path = "./data/prospect_info.txt"
company_info_path = "./data/company_info.txt"
with open(company_info_path, "r") as file:
    company_info = file.read()


################
#    Modular - loading in data
#   Can do Documentloader to load in multiple documents
#    * Look into Memory *
################
def get_company_data():
    loader = TextLoader(prospect_info_path)
    return loader.load()

data = get_company_data()
# print(f"You have {len(data)} main document(s)")
# print(f"Preview of your data:\n\n{data[0].page_content[:80]}")


################
#    Splitting up txt data to avoid token limits, especially
#    for lengthy docs
#    Don't really need at the moment
################
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 800,
    chunk_overlap  = 0
)
docs = text_splitter.split_documents(data)
# print (f"You now have {len(docs)} split documents")



################
#    map_prompt will be the prompt done on the first pass of my documents
#    combine_prompt will be the propmt that is used when you combine the outputs of your map pass
################
map_prompt = """ 
Below is a section of a website about {prospect}

Write a concise summary about {prospect}. If the information is not about {prospect}, exclude it from your summary.

{text}

% CONCISE SUMMARY : 
"""

map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text", "prospect"])


combine_prompt = """
Your goal is to write a personalized outbound email from {sales_rep}, a sales rep at {company} to {prospect}.

A good email is personalized and combines information about the two companies on how they can help each other.
Be sure to use value selling: A sales methodology that focuses on how your product or service will provide value to 
the customer instead of focusing on price or solution.

% INFORMATION ABOUT {company}:
    {company_information}

% INFORMATION ABOUT {prospect}:
    {text}

% INCLUDE THE FOLLOWING PIECES IN YOUR RESPONSE:
    - Start the email with the sentence: "We love that {prospect} helps teams..." then insert what they help teams do.
    - The sentence: "We can help you do XYZ by ABC" Replace XYZ with what {prospect} does and ABC with what {company} does 
    - A 1-2 sentence description about {company}, be brief
    - End your email with a call-to-action such as asking them to set up time to talk more

YOUR RESPONSE: 
"""

combine_prompt_template = PromptTemplate(
    template=combine_prompt, 
    input_variables=["company", "company_information", "sales_rep", "prospect", "text"])


llm = OpenAI(temperature=.5)
# llm = OpenAI(temperature=.5, openai_api_key=openai_api_key)

################
#   Using Summarize to use map reduce in an efficient way, although I am not summarizing
#   By using prompts (map_prompt and combine_prompt), we are giving it more direction
################
chain = load_summarize_chain(
    llm,
    chain_type="map_reduce",
    map_prompt=map_prompt_template,
    combine_prompt=combine_prompt_template,
    verbose=True
)

################
output = chain({
    "input_documents": docs,
    "company": "RapidRoad",
    "company_information" : company_info,
    "sales_rep" : "Michael",
    "prospect" : "GitLab"
})

print(output['output_text'])