from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ai', methods=['POST'])
def ai_core():
    data = request.json
    user_msg = data.get('message', '').lower()
    
    # Database Pengetahuan Harry
    responses = {
        "identitas": "Saya adalah asisten virtual Harry. Harry adalah seorang Web Developer dan System Architect yang ahli dalam Python, Flask, dan infrastruktur Linux.",
        "blockchain": "Memulai pemindaian jaringan. Data real-time berhasil diambil. Saat ini Harry sedang mengembangkan modul untuk integrasi Web3 dan keamanan data terdesentralisasi.",
        "proyek": "Harry telah membangun sistem finansial HitungCuan id dan arsitektur API QRify. Semua proyek fokus pada kecepatan dan skalabilitas.",
        "kontak": "Anda bisa menghubungi Harry melalui email di harry.surya23@gmail.com untuk kolaborasi proyek atau konsultasi teknis.",
        "perintah": "Anda bisa bertanya tentang: profil harry, proyek yang dibuat, teknologi yang dikuasai, harga blockchain, atau cara menghubungi harry."
    }
    
    # Logika Respon
    if any(x in user_msg for x in ["siapa", "profil", "harry"]):
        reply = responses["identitas"]
    elif any(x in user_msg for x in ["blockchain", "crypto", "btc"]):
        try:
            # Mengambil harga Bitcoin asli
            res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            price = res['bpi']['USD']['rate']
            reply = f"{responses['blockchain']} Harga Bitcoin saat ini adalah {price} USD."
        except:
            reply = "Gagal terhubung ke node blockchain. Namun, modul Web3 Harry tetap aktif secara lokal."
    elif any(x in user_msg for x in ["proyek", "hasil kerja", "portfolio"]):
        reply = responses["proyek"]
    elif any(x in user_msg for x in ["kontak", "email", "telepon"]):
        reply = responses["kontak"]
    elif any(x in user_msg for x in ["bantuan", "perintah", "tolong", "bingung"]):
        reply = responses["perintah"]
    else:
        reply = "Perintah tidak dikenal. Ketik perintah untuk melihat apa saja yang bisa saya lakukan."

    return jsonify({
        "reply": reply,
        "time": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
