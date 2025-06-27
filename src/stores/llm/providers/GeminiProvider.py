from ..LLMInterface import LLMInterface
from ..LLMEnums import GeminiEnums
import google.generativeai as genai
import logging

class GeminiProvider(LLMInterface):
    def __init__(self, api_key: str,
                    default_input_max_characters: int=1000,
                    default_generation_max_output_tokens: int=1000,
                    default_generation_temperature: float=0.1):
        
        self.api_key = api_key
        
        self.input_max_character = default_input_max_characters
        self.max_output_tokens = default_generation_max_output_tokens
        self.temperature = default_generation_temperature

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        self.enums = GeminiEnums
        self.logger = logging.getLogger(__name__)

        genai.configure(api_key=self.api_key)

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size

    def process_text(self, text: str):
        return text[:self.input_max_character].strip()

    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None,
                            temperature: float = None):
        
        if not self.generation_model_id:
            self.logger.error("Generation model for CoHere was not set")
            return None

        max_output_tokens = max_output_tokens if max_output_tokens else self.max_output_tokens
        temperature = temperature if temperature else self.temperature

        model = genai.GenerativeModel(
            model_name = self.generation_model_id,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_output_tokens
            }
        )

        chat = model.start_chat(history=chat_history)

        response = chat.send_message(prompt)

        if not response or not response.text:
            self.logger.error("Error while generating text with CoHere")
            return None
        
        return response.text

    def embed_text(self, text: str, document_type: str = None):
        response = genai.embed_content(
            model=self.embedding_model_id,
            content=text,
            task_type=document_type
        )

        if not response or not response["embedding"]:
            self.logger.error("Error while embedding text with CoHere")
            return None
        
        return response["embedding"]

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "parts": self.process_text(prompt)
        }