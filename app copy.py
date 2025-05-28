import dash
from dash import dcc, html, Input, Output, State
import base64
from modules.analyze_chart import analyze_chart
from modules.fundamentals import get_fundamentals, summarize_fundamentals
from modules.macro_sentiment import analyze_macro_sentiment
from modules.decision_engine import generate_signal

app = dash.Dash(__name__)
app.title = "AI Trading Assistant"

app.layout = html.Div([
    html.H2("📊 AI Trading Assistant"),
    dcc.Upload(
        id='upload-image',
        children=html.Button('Carica grafico tecnico'),
        multiple=False
    ),
    dcc.Input(id='ticker', type='text', placeholder='Inserisci Ticker (es. AAPL)', debounce=True),
    html.Button("Analizza", id="analyze-btn", n_clicks=0),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    Input("analyze-btn", "n_clicks"),
    State("upload-image", "contents"),
    State("ticker", "value")
)
def analyze(n_clicks, img_data, ticker):
    if not img_data or not ticker:
        return "Carica un grafico e inserisci un ticker."

    image_data = img_data.split(",")[1]
    image_base64 = f"data:image/png;base64,{image_data}"

    tech_analysis = analyze_chart(image_base64)
    fundamentals = get_fundamentals(ticker.upper())
    fundamental_summary = summarize_fundamentals(fundamentals)
    macro_sent = analyze_macro_sentiment()

    signal = generate_signal(tech_analysis, fundamental_summary, macro_sent)

    return html.Div([
        html.H4("📈 Analisi Tecnica"),
        html.Pre(tech_analysis),
        html.H4("💼 Analisi Fondamentale"),
        html.Pre(fundamental_summary),
        html.H4("🌍 Sentiment Macroeconomico"),
        html.Pre(macro_sent),
        html.H4("🚦 Segnale Operativo"),
        html.Pre(signal)
    ])

if __name__ == "__main__":
    app.run(debug=True)
