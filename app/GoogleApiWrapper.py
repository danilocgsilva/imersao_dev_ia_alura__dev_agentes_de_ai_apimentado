import google.generativeai as genai
import os
        
class GoogleApiWrapper:
    @staticmethod
    def getModels() -> list:
        genai.configure(api_key=os.environ["CHAVE_API_GOOGLE"])
        response = genai.list_models()
        return list(response)
        