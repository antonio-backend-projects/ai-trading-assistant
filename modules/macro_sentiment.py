import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_macro_sentiment() -> str:
    prompt = (
        "Riassumi in breve il sentiment macroeconomico attuale in base alle notizie recenti "
        "(inflazione, tassi, crescita, ecc.)."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sei un economista che analizza il sentiment macro."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Errore nell'analisi macro: {e}"
