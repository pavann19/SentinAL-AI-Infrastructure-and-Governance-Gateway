import numpy as np
import faiss
from core.embeddings import get_embedding
from core.logger import get_logger

logger = get_logger(__name__)

class ScalableVectorStore:
    """
    FAISS-based vector store to replace O(N) list iteration.
    Pre-computes and indexes embeddings for O(log N) retrieval.
    """
    def __init__(self, dimension=768):
        self.dimension = dimension
        # Inner Product with L2 normalized vectors equates to Cosine Similarity
        self.index = faiss.IndexFlatIP(dimension)
        self.texts = []
        
    def add_texts(self, texts):
        if not texts:
            return
        
        logger.info(f"Indexing {len(texts)} texts into FAISS...")
        # Pre-compute all embeddings
        vectors = []
        for t in texts:
            vec = get_embedding(t).cpu().numpy()
            vectors.append(vec)
            
        vec_matrix = np.vstack(vectors).astype('float32')
        faiss.normalize_L2(vec_matrix)
        self.index.add(vec_matrix)
        self.texts.extend(texts)
        
    def get_max_similarity(self, query_vec) -> float:
        """Returns the highest cosine similarity score for the query."""
        if self.index.ntotal == 0:
            return 0.0
            
        vec = query_vec.cpu().numpy().reshape(1, -1).astype('float32')
        faiss.normalize_L2(vec)
        
        scores, _ = self.index.search(vec, 1)
        return float(scores[0][0])

# Global FAISS Stores
threat_store = ScalableVectorStore()
educational_store = ScalableVectorStore()
