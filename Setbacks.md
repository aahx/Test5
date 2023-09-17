# from langchain.document_loaders import UnstructuredURLLoader

`https://python.langchain.com/docs/integrations/document_loaders/url`
- Could not get UnstructuredURLLoader to work
    - Error Message:
        -   exception: Invalid file. The FileType.UNK file type is not supported in partition.
    - Attempted brew install libmagic
        - New Error: nltk_data

# NLTK.download()
- SSL certificate unverifiable
- This affects both UnstructuredURLLoader and SeleniumURLLoader
- As of now will be using simple TextLoader