import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_signal(tech: str, fundamentals: str, macro: str) -> str:
    prompt = (
        "Analizza il contesto seguente e fornisci un segnale operativo BUY, SELL o HOLD con motivazione.\n\n"
        f"📈 Analisi tecnica:\n{tech}\n\n"
        f"💼 Fondamentali:\n{fundamentals}\n\n"
        f"🌍 Macroeconomia:\n{macro}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sei un esperto in investimenti con focus su segnali operativi."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Errore nella generazione del segnale: {e}"
