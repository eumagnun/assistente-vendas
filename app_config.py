import os
from dotenv import load_dotenv

load_dotenv(override=True)
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
LLM_MODEL = os.getenv("LLM_MODEL")
IDENTITY_PLATFORM_REST_API = os.getenv("IDENTITY_PLATFORM_REST_API")
IDENTITY_PLATFORM_API_KEY = os.getenv("IDENTITY_PLATFORM_API_KEY")

MAX_OUTPUT_TOKENS = 8192
TEMPERATURE = 0.1
