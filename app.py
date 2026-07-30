import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, Response, request
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream_response():
    prompt = request.args.get("prompt", "what is java in 30 words")
    print(prompt)
    
    def generate():
        try:
            model = init_chat_model("groq:llama-3.3-70b-versatile")
            for chunk in model.stream(prompt):
                if chunk.content:
                    yield f"data: {json.dumps({'content': chunk.content})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return Response(generate(), mimetype="text/event-stream")

if __name__ == "__main__":
    print("Starting Groq LangChain Streaming Web App on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
