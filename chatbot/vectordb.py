# Import Python Packages
import os
import platform
import textwrap
import requests
from typing import List

import openai
import chromadb
import langchain

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
from langchain.document_loaders import GutenbergLoader
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader



# OpenAI API Key
os.environ["OPENAI_API_KEY"] = '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'



# Configure Chroma
persist_directory = "/content/drive/My Drive/Colab Notebooks/chroma/romeo"