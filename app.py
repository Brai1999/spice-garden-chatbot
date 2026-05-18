from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

business_info = """
You are a customer support assistant 
for a restaurant called Spice Garden.

Opening hours: 11am to 11pm daily
Location: MG Road, Bangalore
Phone: 9876543210
Speciality: North Indian food
Average cost: 500 rupees for two people

Only answer questions about this restaurant.
If you don't know something say 
"Please call us at 9876543210"
"""

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": business_info},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({
        'response': response.choices[0].message.content
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))