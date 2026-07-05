from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/review", methods=["POST"])
def review_code():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "python")

    # Fixed prompt - using triple single quotes
    prompt = f'''
You are an expert code reviewer. Review this {language} code:

{code}

Provide a detailed analysis covering:
1. Brief summary of what the code does
2. Bugs or logical errors (if any)
3. Performance issues
4. Security vulnerabilities
5. Suggestions for improvement
6. Code quality and best practices
'''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return jsonify({"review": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)