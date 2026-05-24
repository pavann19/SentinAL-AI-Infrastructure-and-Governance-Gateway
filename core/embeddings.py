from core.config import EMBEDDING_MODEL

# Lazy-loaded model — loaded only on first use, not at import time.
# This prevents CI failures when the package is mocked or unavailable.
_model = None

def _get_model():
    """Returns a cached SentenceTransformer instance (lazy initialization)."""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer  # noqa: PLC0415
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model

def get_embedding(text: str):
    """Generates a vector for the text."""
    return _get_model().encode(text, convert_to_tensor=True)

def cosine_similarity(vec1, vec2) -> float:
    """Calculates similarity."""
    from sentence_transformers import util  # noqa: PLC0415
    return float(util.pytorch_cos_sim(vec1, vec2).item())