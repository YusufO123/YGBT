from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# AI destekli müzik üretme
@app.route('/generate_music', methods=['POST'])
def generate_music():
    data = request.json
    style = data.get("style", "funk")
    response = requests.post("https://snapmuse.com/tr/ai-music-generator", json={"style": style})
    return jsonify(response.json())

# AI destekli hikaye yazma
@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    theme = data.get("theme", "adventure")
    response = requests.post("https://www.musicmuse.ai/tr", json={"theme": theme})
    return jsonify(response.json())

# AI destekli kitap kapağı tasarlama
@app.route('/generate_cover', methods=['POST'])
def generate_cover():
    data = request.json
    prompt = data.get("prompt", "Bilim kurgu temalı bir kitap kapağı")
    response = requests.post("https://www.canva.com/api", json={"prompt": prompt})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)