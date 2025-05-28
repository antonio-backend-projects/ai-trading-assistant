import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_fundamentals(ticker: str) -> dict:
    api_key = os.getenv("FMP_API_KEY")  # prendi la chiave API dal .env
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0] if data else {}
    except Exception as e:
        return {"error": str(e)}

def summarize_fundamentals(data: dict) -> str:
    if not data:
        return "Errore: nessun dato fondamentale disponibile per il ticker specificato."
    if "error" in data:
        return f"Errore nel recupero dati fondamentali: {data['error']}"
    
    name = data.get("companyName", "N/A")
    pe = data.get("pe", "N/A")
    price = data.get("price", "N/A")
    sector = data.get("sector", "N/A")
    
    return f"{name} opera nel settore {sector}. Prezzo attuale: {price}. P/E: {pe}."

