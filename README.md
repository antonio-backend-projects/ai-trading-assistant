# 🤖 AI Trading Assistant

Un'applicazione Python basata su Dash che consente di caricare grafici di trading (screenshot, immagini) e ottenere analisi tecniche, fondamentali e macroeconomiche con supporto OpenAI.

![Descrizione immagine](images/Screenshot%2025-05-28%140624.png)


## 🚀 Funzionalità

- Upload di immagini di grafici trading
- Analisi tecnica automatizzata con modelli OpenAI
- Estrazione di segnali operativi (buy/sell)
- Integrazione con dati fondamentali e macroeconomici
- UI interattiva realizzata con Dash
- Esecuzione **completamente locale**, chiave API OpenAI gestita tramite `.env`

## 🛠️ Setup rapido

### 1. Clona il repository

```bash
git clone https://github.com/antonio-backend-projects/ai-trading-assistant.git
cd ai-trading-assistant
````

### 2. Crea e attiva un ambiente virtuale

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Imposta la chiave OpenAI

Crea un file `.env` nella root con:

```env
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
FMP_API_KEY=zFWkYJ62X25vn6hz37WTo4cPozQwLsZm
```

> ⚠️ **Non caricare mai `.env` su GitHub!** È già incluso nel `.gitignore`.

---

### 📌 Come ottenere la API key di Financial Modeling Prep (FMP)

1. Vai su [https://financialmodelingprep.com/developer/docs/pricing/](https://financialmodelingprep.com/developer/docs/pricing/)
2. Registrati gratuitamente per un account.
3. Conferma la tua email e accedi al tuo account.
4. Nella dashboard troverai la tua API key gratuita.
5. Copia la chiave e incollala nel file `.env` come mostrato sopra.

---

### 5. Avvia l'applicazione

```bash
python app.py
```

---

## 📁 Struttura del progetto

```bash
ai-trading-assistant/
│
├── app.py                 # Entrypoint dell'app Dash
├── analysis.py            # Logica di analisi immagini e trading
├── utils.py               # Funzioni di utilità
├── .env                   # Chiave OpenAI (non tracciato)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Modelli e fonti usate

* [OpenAI GPT](https://platform.openai.com/)
* [LangChain](https://www.langchain.com/)
* [Dash by Plotly](https://dash.plotly.com/)
* [Dati macro e fondamentali](#) *(in base alla tua implementazione)*

---

## 📜 Licenza

[MIT License](LICENSE)
