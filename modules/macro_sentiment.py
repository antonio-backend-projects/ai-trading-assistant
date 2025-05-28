from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_macro_sentiment() -> str:
    prompt = (
        "Assumi di essere un economista che ha appena letto le ultime notizie di oggi su inflazione, tassi e crescita. "
        "In base a queste informazioni ipotetiche, fornisci una breve analisi del sentiment macroeconomico attuale, "
        "come faresti in una nota interna di una banca d'investimento."
    )

    try:
        response = client.chat.completions.create(
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
