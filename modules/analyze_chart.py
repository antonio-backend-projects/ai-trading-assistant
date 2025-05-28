from openai import OpenAI
from PIL import Image
import io
import base64
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_chart(image_base64: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Sei un analista tecnico esperto."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analizza questo grafico e identifica pattern tecnici rilevanti."},
                        {"type": "image_url", "image_url": {"url": image_base64}},
                    ],
                },
            ],
            max_tokens=800
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Errore durante l'analisi del grafico: {e}"
