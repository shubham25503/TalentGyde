import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from huggingface_hub import login
from app.config import settings

class ModelHandler:
    def __init__(self):
        login(settings.SECRET_KEY)
        
        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True
        )

        self.tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME) # 8,192 tokens 
        self.model = AutoModelForCausalLM.from_pretrained(
            settings.MODEL_NAME,
            quantization_config=self.bnb_config,
            device_map="auto",
        )
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

model_handler = ModelHandler()
# model_handler = None
