from dotenv import load_dotenv
import os

# Caminho absoluto do arquivo .env
from pathlib import Path

env_path = Path('.') / '.env'  # Garante que o caminho está correto
load_dotenv(dotenv_path=env_path)

# Testa novamente
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASS:", os.getenv("DB_PASS"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))