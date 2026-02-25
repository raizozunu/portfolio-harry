from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ai', methods=['POST'])
def ai_core():
    data = request.json
    user_msg = data.get('message', '').lower()
    
    # Knowledge Engine
    responses = {
        "identitas": "Saya adalah asisten AI Harry, seorang Web Developer yang ahli dalam membangun arsitektur sistem backend berperforma tinggi.",
        "portfolio": "Website ini adalah portofolio resmi Harry untuk menampilkan proyek Web Development dan keahlian sistemnya.",
        "tech": "Harry menguasai Python, Flask, Linux Server, dan Database Management.",
        "tema": "Anda bisa mengubah tema menjadi Gelap, Terang, atau Otomatis melalui tombol di navigasi atas."
    }
    
    # Logic Smart Reply
    if any(x in user_msg for x in ["siapa", "harry", "developer"]):
        reply = responses["identitas"]
    elif any(x in user_msg for x in ["portfolio", "website apa"]):
        reply = responses["portfolio"]
    elif any(x in user_msg for x in ["stack", "bahasa", "teknologi"]):
        reply = responses["tech"]
    elif any(x in user_msg for x in ["tema", "warna", "gelap", "terang"]):
        reply = responses["tema"]
    else:
        reply = f"Menarik. Sebagai Web Developer, Harry selalu mencari solusi untuk '{user_msg}'. Ada hal spesifik tentang sistem yang ingin Anda diskusikan?"

    return jsonify({
        "reply": reply,
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
        "status": "Online"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
