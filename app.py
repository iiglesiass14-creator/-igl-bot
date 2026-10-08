import os, requests
from flask import Flask, request
app = Flask(__name__)
VERIFY_TOKEN = "IGL2025"
PHONE_ID = "1352756234588527"
TOKEN = os.environ.get("WHATSAPP_TOKEN")
def enviar(to, texto):
    url = f"https://graph.facebook.com/v19.0/{PHONE_ID}/messages"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    data = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": texto}}
    requests.post(url, headers=headers, json=data)
@app.route("/webhook", methods=["GET"])
def v():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Error", 403
@app.route("/webhook", methods=["POST"])
def r():
    data = request.get_json()
    try:
        m = data['entry'][0]['changes'][0]['value']['messages'][0]
        tel = m['from']
        txt = m['text']['body'].lower()
        if "hola" in txt:
            resp = "Hola! Soy IGL 🏢\n1️⃣ Generar Boleta SIN Importe\nResponde 1"
        elif txt == "1":
            resp = "Mandame Nombre y CUIT para boleta sin importe"
        else:
            resp = "Recibido. Generando boleta..."
        enviar(tel, resp)
    except:
        pass
    return "ok", 200
@app.route("/")
def i():
    return "IGL Activo"
