import os
import sys
from dotenv import load_dotenv

from utils.config_loader import load_config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    
    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config = load_config()
        log.info("Configuration loaded successfully", config_keys=list(self.config.keys())) 
    
    def _validate_env(self):
        """  
        Validate necessary environment variables.
        Ensure API keys exists
        """ 
        required_vars = ['GOOGLE_API_KEY', 'GROQ_API_KEY']
        self.api_keys = {key: os.getenv(key) for key in required_vars}
        missing = [k for k, v in self.api_keys.items() if not v]
        if missing:
            log.error("Missing environment variables", missing_vars=missing)
            raise DocumentPortalException("Missing environment variables", sys)
        log.info("Environment variables validated", available_keys=[k for k in self.api_keys if self.api_keys[k]])
    
    def load_embeddings(self):
        """ 
        Load and return the embedding model.
        """ 
        try:
            log.info("Loading embedding model...") 
            model_name = self.config['embedding_model']['model_name']
        except Exception as e:
            log.error("Error loading embedding model", error=str(e))
            raise
    
    def load_llm(self):
        pass
    
    
obj = ModelLoader()