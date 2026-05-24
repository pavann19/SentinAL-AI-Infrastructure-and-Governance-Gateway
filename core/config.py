# core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Capability Tiers
    CAPABILITY_GENERAL: str = "GENERAL"       # Formerly 'student'
    CAPABILITY_ELEVATED: str = "ELEVATED"     # Formerly 'researcher'
    CAPABILITY_INTERNAL: str = "INTERNAL"     # Formerly 'admin'

    # Security Thresholds
    SEMANTIC_THRESHOLD_HIGH: float = 0.48
    SEMANTIC_THRESHOLD_MEDIUM: float = 0.22
    EDUCATIONAL_THRESHOLD: float = 0.45
    DOMAIN_THRESHOLD: float = 0.22
    CACHE_SIMILARITY_THRESHOLD: float = 0.95
    META_INTENT_THRESHOLD: float = 0.40
    
    # Execution Environment
    OLLAMA_API_URL: str = "http://localhost:11434/api/generate"
    OLLAMA_MODEL: str = "mistral"
    EMBEDDING_MODEL: str = "all-mpnet-base-v2"
    
    # File Paths
    POLICY_FILE: str = "policies.json"
    POLICY_RULES_FILE: str = "policy_rules.json"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

# For backwards compatibility with existing imports:
CAPABILITY_GENERAL = settings.CAPABILITY_GENERAL
CAPABILITY_ELEVATED = settings.CAPABILITY_ELEVATED
CAPABILITY_INTERNAL = settings.CAPABILITY_INTERNAL
SEMANTIC_THRESHOLD_HIGH = settings.SEMANTIC_THRESHOLD_HIGH
SEMANTIC_THRESHOLD_MEDIUM = settings.SEMANTIC_THRESHOLD_MEDIUM
EDUCATIONAL_THRESHOLD = settings.EDUCATIONAL_THRESHOLD
DOMAIN_THRESHOLD = settings.DOMAIN_THRESHOLD
CACHE_SIMILARITY_THRESHOLD = settings.CACHE_SIMILARITY_THRESHOLD
META_INTENT_THRESHOLD = settings.META_INTENT_THRESHOLD

# New configuration properties exported directly:
OLLAMA_API_URL = settings.OLLAMA_API_URL
OLLAMA_MODEL = settings.OLLAMA_MODEL
EMBEDDING_MODEL = settings.EMBEDDING_MODEL
POLICY_FILE = settings.POLICY_FILE
POLICY_RULES_FILE = settings.POLICY_RULES_FILE