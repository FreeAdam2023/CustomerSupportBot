"""
@Time ： 2024-10-27
@Auth ： Adam Lyu
"""
import re
import os
import requests
import numpy as np
import openai
from langchain_core.tools import tool
from dotenv import load_dotenv
from utils.logger import logger  # 导入自定义日志记录工具

load_dotenv()  # 加载 .env 文件中的环境变量

logger.info("Starting FAQ data retrieval from URL.")
try:
    response = requests.get(
        "https://storage.googleapis.com/benchmarks-artifacts/travel-db/swiss_faq.md"
    )
    response.raise_for_status()
    faq_text = response.text
    logger.info("FAQ data successfully retrieved.")
except requests.RequestException as e:
    logger.error(f"Failed to retrieve FAQ data: {e}")
    faq_text = ""

docs = [{"page_content": txt} for txt in re.split(r"(?=\n##)", faq_text)]
logger.debug(f"Parsed documents: {docs}")


class VectorStoreRetriever:
    def __init__(self, docs: list, vectors: list, oai_client):
        self._arr = np.array(vectors)
        self._docs = docs
        self._client = oai_client
        logger.info("VectorStoreRetriever initialized with documents and vectors.")

    @classmethod
    def from_docs(cls, docs, oai_client):
        logger.info("Creating embeddings from documents.")
        embeddings = oai_client.embeddings.create(
            model="text-embedding-3-small", input=[doc["page_content"] for doc in docs]
        )
        vectors = [emb.embedding for emb in embeddings.data]
        logger.info("Embeddings created successfully.")
        return cls(docs, vectors, oai_client)

    def query(self, query: str, k: int = 5) -> list[dict]:
        logger.info(f"Executing query with top {k} results.")
        try:
            embed = self._client.embeddings.create(
                model="text-embedding-3-small", input=[query]
            )
            scores = np.array(embed.data[0].embedding) @ self._arr.T
            top_k_idx = np.argpartition(scores, -k)[-k:]
            top_k_idx_sorted = top_k_idx[np.argsort(-scores[top_k_idx])]
            results = [
                {**self._docs[idx], "similarity": scores[idx]} for idx in top_k_idx_sorted
            ]
            logger.info(f"Query returned {len(results)} results.")
            return results
        except Exception as e:
            logger.error(f"Error during query execution: {e}")
            return []


try:
    retriever = VectorStoreRetriever.from_docs(
        docs, openai.Client(api_key=os.getenv('OPENAI_API_KEY'))
    )
    logger.info("VectorStoreRetriever successfully initialized.")
except Exception as e:
    logger.error(f"Failed to initialize VectorStoreRetriever: {e}")
    retriever = None


@tool
def lookup_policy(query: str) -> str:
    """Consult the company policies to check whether certain options are permitted.
    Use this before making any flight changes performing other 'write' events."""
    if not retriever:
        logger.error("Retriever is not initialized. Cannot perform lookup.")
        return "Policy lookup failed due to initialization error."

    logger.info(f"Looking up policy for query: '{query}'")
    docs = retriever.query(query, k=2)
    result = "\n\n".join([doc["page_content"] for doc in docs])
    logger.info("Policy lookup completed.")
    return result
