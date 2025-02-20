from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

# Hugging Face API Key
API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def generate_logo(prompt):
    """Send request to Hugging Face API"""
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')  # Convert image to base64
    else:
        return None

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt")
    image_data = generate_logo(prompt)

    if image_data:
        return jsonify({"image": image_data})
    else:
        return jsonify({"error": "Failed to generate image."})

if __name__ == "__main__":
    app.run(debug=True)
