
import os
from dotenv import load_dotenv

load_dotenv()

print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))
print("API Key:", os.getenv("AZURE_OPENAI_API_KEY"))
print("Deployment:", os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"))
print("Version:", os.getenv("AZURE_OPENAI_API_VERSION"))