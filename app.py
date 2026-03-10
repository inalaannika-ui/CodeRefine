from flask import Flask, render_template, request, jsonify
from utils import refine_code, check_code_quality,explain_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_code():
    data = request.json
    code = data.get("code")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    refined = refine_code(code)
    quality = check_code_quality(code)
    explanation=explain_code(code)
    score=score_code(code)
    suggestions=suggest_improvements(code)
    complexity=detect_complexity(code)

    return jsonify({
        "original_code": code,
        "refined_code": refined,
        "analysis": quality,
        "explanation":explanation,
        "score": score,
        "suggestions": suggestions,
        "complexity": complexity
    })

if __name__ == "__main__":
    app.run(debug=True)
    