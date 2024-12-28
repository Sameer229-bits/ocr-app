from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

# Azure Form Recognizer credentials
endpoint = "https://docuaipoc.cognitiveservices.azure.com/" 
key = "1ttqQYP9EHB5GukN824pCiATLUX13j9rwHAN25kUvhWGE0R7r5lQJQQJ99ALACGhslBXJ3w3AAALACOGuYpQ"

def extract_text(file_path):
    client = DocumentAnalysisClient(endpoint, AzureKeyCredential(key))

    # Read the file as binary
    with open(file_path, "rb") as f:
        poller = client.begin_analyze_document("prebuilt-read", document=f)
        result = poller.result()

    # Extracted text
    extracted_text = ""
    for page in result.pages:
        for line in page.lines:
            extracted_text += line.content + "\n"

    return extracted_text