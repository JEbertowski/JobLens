import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024
