# 🤖 AI Trading Assistant

Un'applicazione Python basata su Dash che consente di caricare grafici di trading (screenshot, immagini) e ottenere analisi tecniche, fondamentali e macroeconomiche con supporto OpenAI.

![Descrizione immagine](images/Screenshot%202025-05-28%20135545.png)


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
```

> ⚠️ **Non caricare mai `.env` su GitHub!** È già incluso nel `.gitignore`.

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
