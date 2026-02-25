from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ai', methods=['POST'])
def ai_core():
    data = request.json
    user_msg = data.get('message', '').lower()
    
    # Brain Logic Harry (Knowledge Base)
    knowledge = {
        "identitas": ["siapa", "nama", "profil", "harry", "developer", "pengembang", "siapa anda"],
        "portofolio": ["apa ini", "website apa", "fungsi", "tujuan", "portfolio"],
        "proyek": ["project", "karya", "buat", "hitungcuan", "qrify", "hasil kerja"],
        "teknologi": ["stack", "bahasa", "coding", "python", "flask", "database", "tech"],
        "layanan": ["jasa", "sewa", "hire", "kerja", "bangun", "sistem", "kontak"]
    }
    
    if any(word in user_msg for word in knowledge["identitas"]):
        reply = "Saya adalah asisten virtual Harry. Harry adalah seorang Web Developer profesional yang berfokus pada arsitektur backend dan sistem skala besar."
    elif any(word in user_msg for word in knowledge["portofolio"]):
        reply = "Ini adalah portofolio resmi Harry. Dirancang untuk mendemonstrasikan keahlian dalam Full-Stack Development dan Sistem Neural."
    elif any(word in user_msg for word in knowledge["proyek"]):
        reply = "Harry telah membangun HitungCuan id dan QRify. Semua proyek mengutamakan stabilitas dan performa tinggi."
    elif any(word in user_msg for word in knowledge["teknologi"]):
        reply = "Teknologi utama yang digunakan meliputi Python, Flask, PostgreSQL, Docker, dan deployment di Arch Linux."
    elif any(word in user_msg for word in knowledge["layanan"]):
        reply = "Harry melayani konsultasi arsitektur web dan jasa backend development. Silakan hubungi via email di harry.surya23@gmail.com."
    else:
        reply = f"Pertanyaan '{user_msg}' telah diterima. Sebagai Web Developer, Harry selalu siap memberikan solusi teknis terbaik untuk Anda."

    return jsonify({
        "reply": reply,
        "time": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
