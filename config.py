# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback_secret_key')  # Optional fallback for local development

# Note: The fallback key is for development purposes only and should not be used in production.
