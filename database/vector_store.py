from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from utils.embeddings import get_embeddings


def create_vector_db():

    loader = PyPDFLoader("documents/kyc_rules.pdf")

    docs = loader.load()

    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)

    return db